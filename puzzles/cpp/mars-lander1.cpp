#include <iostream>

using namespace std;

int main() {
  int surfaceN;
  cin >> surfaceN; cin.ignore();
  for (int i = 0; i < surfaceN; i++) {
    int landX;
    int landY;
    cin >> landX >> landY; cin.ignore();
  }

  // game loop
  while (true) {
    int X;
    int Y;
    int hSpeed;
    int vSpeed; // the vertical speed (in m/s), can be negative.
    int fuel;
    int angle; // the rotation angle in degrees (-90 to 90).
    int power; // the thrust power (0 to 4).
    cin >> X >> Y >> hSpeed >> vSpeed >> fuel >> angle >> power; cin.ignore();

    angle = 0;
    if (vSpeed <= -40) {
      power = 4;
    } else {
      power = 0;
    }

    cout << angle << " " << power << endl;
  }
}
