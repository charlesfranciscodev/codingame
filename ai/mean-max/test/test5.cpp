#include <iostream>

#include "../../src/referee.cpp"

using namespace std;

int main() {
  Referee referee;
  referee.readGameInfo();
  Referee refereeCopy(referee);

  vector<Action*> actions0 = {new Action(), new Action(), new Action()};
  refereeCopy.assignActions(0, actions0);

  int power = MAX_THRUST;

  vector<Action*> actions1 = {
    new Action(2919, -1174, false, power, "TEST"),
    new Action(-4088, -3322, false, power, "TEST"),
    new Action(2162, -4394, false, power, "TEST")
  };
  refereeCopy.assignActions(1, actions1);

  vector<Action*> actions2 = {
    new Action(2145, -835, false, power, "TEST"),
    new Action(-4371, -3415, false, power, "TEST"),
    new Action(2145, -835, "TEST")
  };
  refereeCopy.assignActions(2, actions2);

  refereeCopy.updateGame();

  cout << refereeCopy.toString();
}
