#include <iostream>
#include <vector>

using namespace std;

int main() {
  int width; // width of the building.
  int height; // height of the building.
  cin >> width >> height; cin.ignore();
  int n;
  cin >> n; cin.ignore();
  int x, y;
  cin >> x >> y; cin.ignore();
  int minX = 0;
  int maxX = width - 1;
  int minY = 0;
  int maxY = height - 1;

  // game loop
  while (true) {
    string bombDir;
    cin >> bombDir; cin.ignore();

    if (bombDir == "U") {
      minX = maxX = x;
      maxY = y - 1;
    } else if (bombDir == "UR") {
      minX = x + 1;
      maxY = y - 1;
    } else if (bombDir == "R") {
      minY = maxY = y;
      minX = x + 1;
    } else if (bombDir == "DR") {
      minX = x + 1;
      minY = y + 1;
    } else if (bombDir == "D") {
      minX = maxX = x;
      minY = y + 1;
    } else if (bombDir == "DL") {
      maxX = x - 1;
      minY = y + 1;
    } else if (bombDir == "L") {
      minY = maxY = y;
      maxX = x - 1;
    } else if (bombDir == "UL") {
      maxX = x - 1;
      maxY = y - 1;
    }

    x = (minX + maxX) / 2;
    y = (minY + maxY) / 2;
    // the location where Batman should jump to.
    cout << x << " " << y << endl;
  }
}
