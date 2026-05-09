#include <iostream>
#include <vector>

using namespace std;

const char EMPTY = '.';
const char TARGET = '@';
const char WALL = '#';
const int EXPLOSTION_TIME = 3;
const int BOMB_RANGE = 3;

class Node {
  public:
    int x, y;
    char symbol;
    bool destroy = false;
    int timeToDetonation = EXPLOSTION_TIME;
    bool invalid = false;

    Node(int column, int row, char c) : x(column), y(row), symbol(c) {}

    void copy(const Node& other) {
      x = other.x;
      y = other.y;
      symbol = other.symbol;
      destroy = other.destroy;
      timeToDetonation = other.timeToDetonation;
      invalid = other.invalid;
    }

    Node(const Node& other) {
      copy(other);
    }

    ~Node() {}

    Node& operator = (const Node& other) {
      if (this != &other) {
        copy(other);
      }
      return *this;
    }

    bool isValidTarget() {
      return symbol == TARGET && !destroy;
    }

    bool isValidFutureBombPlacement() {
      return !invalid && (symbol == EMPTY || (symbol == TARGET && destroy));
    }

    void update() {
      if (symbol == TARGET && destroy) {
        timeToDetonation--;
        if (timeToDetonation == 0) {
          symbol = EMPTY;
        }
      }
    }

  friend ostream& operator << (ostream&, const Node&);
};

ostream& operator << (ostream& os, const Node& node) {
  os << node.symbol;
  return os;
}

class Grid {
  public:
    int width = 0; // width of the firewall grid
    int height = 0; // height of the firewall grid
    vector<vector<Node>> nodes;

    Grid() {}

    void copy(const Grid& other) {
      width = other.width;
      height = other.height;
      for (int y = 0; y < height; y++) {
        vector<Node> row;
        for (int x = 0; x < width; x++) {
          row.push_back(other.nodes[y][x]);
        }
        nodes.push_back(row);
      }
    }

    Grid(const Grid& other) {
      copy(other);
    }

    ~Grid() {}

    Grid& operator = (const Grid& other) {
      if (this != &other) {
        copy(other);
      }
      return *this;
    }

    void destroy(int x, int y) {
      nodes[y][x].destroy = true;
    }

    bool isValidTarget(int x, int y) {
      return nodes[y][x].isValidTarget();
    }

    bool isValidFutureBombPlacement(int x, int y) {
      return nodes[y][x].isValidFutureBombPlacement();
    }

    bool isDestroyed() {
      for (int y = 0; y < height; y++) {
        for (int x = 0; x < width; x++) {
          if (nodes[y][x].symbol == TARGET) {
            return false;
          }
        }
      }
      return true;
    }

    void update() {
      for (int y = 0; y < height; y++) {
        for (int x = 0; x < width; x++) {
          nodes[y][x].update();
        }
      }
    }

    // update the state of the grid
    // Precondition: The node at (x, y) should be a valid target.
    void placeBomb(int x, int y) {
      // BOTTOM
      for (int i = y + 1; i <= y + BOMB_RANGE && i < height; i++) {
        if (isValidTarget(x, i)) {
          destroy(x, i);
        } else if (nodes[i][x].symbol == WALL) {
          break;
        }
      }

      // TOP
      for (int j = y - 1; j >= y - BOMB_RANGE && j >= 0; j--) {
        if (isValidTarget(x, j)) {
          destroy(x, j);
        } else if (nodes[j][x].symbol == WALL) {
          break;
        }
      }

      // RIGHT
      for (int k = x + 1; k <= x + BOMB_RANGE && k < width; k++) {
        if (isValidTarget(k, y)) {
          destroy(k, y);
        } else if (nodes[y][k].symbol == WALL) {
          break;
        }
      }

      // LEFT
      for (int m = x - 1; m >= x - BOMB_RANGE && m >= 0; m--) {
        if (isValidTarget(m, y)) {
          destroy(m, y);
        } else if (nodes[y][m].symbol == WALL) {
          break;
        }
      }
    }

    // score = number of targets destroyed
    // Precondition: The node at (x, y) should be a valid target.
    int placeBombScore(int x, int y) {
      int score = 0;

      // BOTTOM
      for (int i = y + 1; i <= y + BOMB_RANGE && i < height; i++) {
        if (isValidTarget(x, i)) {
          score++;
        } else if (nodes[i][x].symbol == WALL) {
          break;
        }
      }

      // TOP
      for (int j = y - 1; j >= y - BOMB_RANGE && j >= 0; j--) {
        if (isValidTarget(x, j)) {
          score++;
        } else if (nodes[j][x].symbol == WALL) {
          break;
        }
      }

      // RIGHT
      for (int k = x + 1; k <= x + BOMB_RANGE && k < width; k++) {
        if (isValidTarget(k, y)) {
          score++;
        } else if (nodes[y][k].symbol == WALL) {
          break;
        }
      }

      // LEFT
      for (int m = x - 1; m >= x - BOMB_RANGE && m >= 0; m--) {
        if (isValidTarget(m, y)) {
          score++;
        } else if (nodes[y][m].symbol == WALL) {
          break;
        }
      }

      return score;
    }

    // greedy solution: pick the bomb placement with the highest score
    Node* pickBombPlacement() {
      int maxScore = 0;
      Node* maxNode = nullptr;
      for (int y = 0; y < height; y++) {
        for (int x = 0; x < width; x++) {
          if (isValidFutureBombPlacement(x, y)) {
            int score = placeBombScore(x, y);
            if (score > maxScore) {
              maxScore = score;
              maxNode = &(nodes[y][x]);
            }
          }
        }
      }
      return maxNode;
    }

  friend ostream& operator << (ostream&, const Grid&);
};

ostream& operator << (ostream& os, const Grid& grid) {
  for (int y = 0; y < grid.height; y++) {
    for (int x = 0; x < grid.width; x++) {
      os << grid.nodes[y][x];
    }
    os << endl;
  }
  return os;
}

class VoxCodei {
  public:
    Grid grid;
    int nbRounds = 0; // number of rounds left before the end of the game
    int nbBombs = 0; // number of bombs left
    int round = 1; // current round

  VoxCodei() {}

  void readInitInput() {
    cin >> grid.width >> grid.height; cin.ignore();
    for (int y = 0; y < grid.height; y++) {
      string mapRow; // one line of the firewall grid
      getline(cin, mapRow);
      vector<Node> row;
      for (int x = 0; x < mapRow.size(); x++) {
        row.push_back(Node(x, y, mapRow[x]));
      }
      grid.nodes.push_back(row);
    }
  }

  void gameLoop() {
    while (true) {
      cerr << grid << endl;
      cin >> nbRounds >> nbBombs; cin.ignore();
      playTurn();
      round++;
    }
  }

  void playTurn() {
    Node* node = grid.pickBombPlacement();

    // simulate everything fox max, if it doesn't work out, backtrack
    if (node != nullptr && round == 1 && !simulateTurn(node->x, node->y)) {
      node->invalid = true;
      node = grid.pickBombPlacement();
    }

    // validate bomb placement for next turn
    if (node == nullptr || node->symbol != EMPTY) {
      cout << "WAIT" << endl; // wait until it gets destroyed
    } else {
      grid.placeBomb(node->x, node->y);
      cout << node->x << ' ' << node->y << endl;
    }
    grid.update();
  }

  bool simulateTurn(int x, int y) {
    int bombs = nbBombs;
    int rounds = nbRounds;
    Grid gridCopy(grid);
    Node* current = &(gridCopy.nodes[y][x]);

    while (bombs != 0 && rounds != 0 && !gridCopy.isDestroyed()) {
      if (current != nullptr && current->symbol == EMPTY) {
        gridCopy.placeBomb(current->x, current->y);
        bombs--;
      }
      gridCopy.update();
      rounds--;
      current = gridCopy.pickBombPlacement();
    }

    while (rounds != 0 && !gridCopy.isDestroyed()) {
      gridCopy.update();
      rounds--;
    }

    return gridCopy.isDestroyed();
  }
};

int main() {
  VoxCodei voxCodei;
  voxCodei.readInitInput();
  voxCodei.gameLoop();
}
