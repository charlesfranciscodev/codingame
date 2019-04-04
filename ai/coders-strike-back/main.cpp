// Silver League

#include <iostream>
#include <math.h>

using namespace std;

class Point {
  public:
    float x = 0;
    float y = 0;

    Point(int x, int y) {
      this->x = (float) x;
      this->y = (float) y;
    }

    float distance(Point point) {
      float xDiff = x - point.x;
      float yDiff = y - point.y;
      return xDiff * xDiff + yDiff * yDiff;
    }

    float distance2(Point point) {
      return sqrt(distance(point));
    }
};

int main() {
  bool boostAvailable = true;

  // game loop
  while (1) {
    int x;
    int y;
    int nextCheckpointX;
    int nextCheckpointY;
    int nextCheckpointDist;
    int nextCheckpointAngle;
    cin >> x >> y >> nextCheckpointX >> nextCheckpointY >> nextCheckpointDist >> nextCheckpointAngle; cin.ignore();
    Point myPoint(x, y);
    Point nextCheckpoint(nextCheckpointX, nextCheckpointY);
    int opponentX;
    int opponentY;
    cin >> opponentX >> opponentY; cin.ignore();
    Point enemyPoint(opponentX, opponentY);

    // Write an action using cout. DON'T FORGET THE "<< endl"
    // To debug: cerr << "Debug messages..." << endl;

    int thrust = 100;
    bool boost = false;
    string message = "SPEED";

    if (nextCheckpointAngle > 90 or nextCheckpointAngle < -90) {
      thrust = 0;
      message = "SLOW";
    } else {
      if (boostAvailable && nextCheckpointDist >= 7500 && abs(nextCheckpointAngle) <= 5) {
        cerr << nextCheckpointDist << endl;
        boost = true;
        message = "BOOST";
      }
    }

    if (!boost) {
      cout << nextCheckpointX << " " << nextCheckpointY << " " << thrust << " " << message << endl;
    } else {
      cout << nextCheckpointX << " " << nextCheckpointY << " " << "BOOST " << message << endl;
    }

    if (boost) {
      boostAvailable = false;
    }
  }
}
