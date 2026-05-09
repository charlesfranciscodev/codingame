#include <iostream>

using namespace std;

int main() {
  int lightX; // the X position of the light of power
  int lightY; // the Y position of the light of power
  int thorX; // Thor's starting X position
  int thorY; // Thor's starting Y position
  cin >> lightX >> lightY >> thorX >> thorY; cin.ignore();

  // game loop
  while (true) {
    string direction = "";
    int remainingTurns; // The remaining amount of turns Thor can move. Do not remove this line.
    cin >> remainingTurns; cin.ignore();

    if (thorY > lightY) {
      direction += "N";
      thorY--;
    } else if (thorY < lightY) {
      direction += "S";
      thorY++;
    }

    if (thorX > lightX) {
      direction += "W";
      thorX--;
    } else if (thorX < lightX) {
      direction += "E";
      thorX++;
    }

    // A single line providing the move to be made: N NE E SE S SW W or NW
    cout << direction << endl;
  }
}
