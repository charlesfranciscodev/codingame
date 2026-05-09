#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cctype>

using namespace std;

enum Result {
  PLAYER1,
  PLAYER2,
  WAR
};

class Game;

class Card {
  private:
    string value;
    string suit;

  public:
    Card(string v, string s) : value(v), suit(s) {}

    Card(const Card& other) : value(other.value), suit(other.suit) {}

    ~Card() {}

    int intValue() const {
      if (all_of(value.begin(), value.end(), ::isdigit)) {
        return stoi(value);
      }
      if (value == "J") {
        return 11;
      } else if (value == "Q") {
        return 12;
      } else if (value == "K") {
        return 13;
      } else {
        return 14; // A
      }
    }

    Card& operator = (const Card& other) {
      if (this != &other) {
        value = other.value;
        suit = other.suit;
      }
      return *this;
    }

    bool operator < (const Card& other) const {
      return intValue() < other.intValue();
    }
  
  friend class Game;
};

class Game {
  private:
    vector<Card> deck1;
    vector<Card> deck2;
    int nbRounds = 0;

  public:
    void readDeck(vector<Card>& deck) {
      int nbCards;
      cin >> nbCards; cin.ignore();
      for (int i = 0; i < nbCards; i++) {
        string valueSuit;
        cin >> valueSuit; cin.ignore();
        string value = valueSuit.substr(0, valueSuit.size() - 1);
        string suit = valueSuit.substr(valueSuit.size() - 1, 1);
        Card card(value, suit);
        deck.push_back(card);
      }
    }

    void readGameInput() {
      readDeck(deck1);
      readDeck(deck2);
    }

    vector<Card> rotate(vector<Card>& deck, int index) {
      vector<Card> rotatedDeck;
      for (int i = index; i < deck.size(); i++) {
        rotatedDeck.push_back(deck[i]);
      }
      for (int j = 0; j < index; j++) {
        rotatedDeck.push_back(deck[j]);
      }
      return rotatedDeck;
    }

    void checkGameOver() {
      if (deck1.size() == 0) {
        cout << 2 << ' ' << nbRounds << endl;
        exit(0);
      }
      if (deck2.size() == 0) {
        cout << 1 << ' ' << nbRounds << endl;
        exit(0);
      }
    }

    // Returns the result of one game turn
    Result playTurn(int index) {
      if (index > deck1.size() || index > deck2.size()) {
        cout << "PAT" << endl;
        exit(0);
      }

      checkGameOver();

      if (deck2[index] < deck1[index]) {
        return PLAYER1;
      } else if (deck1[index] < deck2[index]) {
        return PLAYER2;
      } else {
        return WAR;
      }
    }

    void play() {
      int index = 0;
      while (true) {
        Result result = playTurn(index);
        int rotateIndex = index + 1;
        if (result == PLAYER1) {
          nbRounds++;
          deck1 = rotate(deck1, rotateIndex);
          // take other player's cards
          for (int i = 0; i < rotateIndex; i++) {
            deck1.push_back(deck2[i]);
          }
          // remove other player's cards
          deck2.erase(deck2.begin(), deck2.begin() + rotateIndex);
          index = 0;
        } else if (result == PLAYER2) {
          nbRounds++;
          // take other player's cards
          for (int i = 0; i < rotateIndex; i++) {
            deck2.push_back(deck1[i]);
          }
          // remove other player's cards
          deck1.erase(deck1.begin(), deck1.begin() + rotateIndex);
          deck2 = rotate(deck2, rotateIndex);
          index = 0;
        } else {
          index += 4; // WAR
        }
      }
    }

    void showDecks() {
      cerr << "round #" << nbRounds << endl;
      for (auto card : deck1) {
        cerr << card.value << card.suit << " ";
      }
      cerr << endl;
      for (auto card : deck2) {
        cerr << card.value << card.suit << " ";
      }
      cerr << endl;
    }
};

int main() {
  Game game;
  game.readGameInput();
  game.play();
}
