#include <iostream>
#include <vector>

using namespace std;

int main() {
  const char EMPTY = '.';
  const char NODE = '0';
  vector<string> grid;

  int width; // the number of cells on the X axis
  cin >> width; cin.ignore();
  int height; // the number of cells on the Y axis
  cin >> height; cin.ignore();
  for (int i = 0; i < height; i++) {
    string line;
    getline(cin, line);
    grid.push_back(line);
  }

  for (int y = 0; y < height; y++) {
    for (int x = 0; x < width; x++) {
      if (grid[y][x] == NODE) {
        // node
        cout << x << ' ' << y << ' ';

        // right neighbor
        char neighbor = EMPTY;
        for (int neighbor_x = x + 1; neighbor_x < width; neighbor_x++) {
          neighbor = grid[y][neighbor_x];
          if (neighbor == NODE) {
            cout << neighbor_x << ' ' << y << ' ';
            break;
          }
        }

        if (neighbor == EMPTY) {
          cout << "-1 -1 ";
        }

        // bottom neighbor
        neighbor = EMPTY;
        for (int neighbor_y = y + 1; neighbor_y < height; neighbor_y++) {
          neighbor = grid[neighbor_y][x];
          if (neighbor == NODE) {
            cout << x << ' ' << neighbor_y << ' ';
            break;
          }
        }

        if (neighbor == EMPTY) {
          cout << "-1 -1 ";
        }

        cout << endl;
      }
    }
  }
}
