#include <iostream>

using namespace std;

int main() {
  // game loop
  while (true) {
    int max = -1;
    int indexMax = 0;
    for (int i = 0; i < 8; i++) {
      int height; // represents the height of one mountain.
      cin >> height; cin.ignore();
      if (height > max) {
        max = height;
        indexMax = i;
      }
    }

    cout << indexMax << endl; // The index of the mountain to fire on.
  }
}
