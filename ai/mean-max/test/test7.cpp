#include <iostream>

#include "../../src/referee.cpp"

using namespace std;

int main() {
  Referee referee;
  referee.readGameInfo();
  Referee refereeCopy(referee);

  // depth 1
  vector<Action*> actions0 = {new Action(), new Action(), new Action()};
  refereeCopy.assignActions(0, actions0);

  int power = MAX_THRUST;

  vector<Action*> actions1 = {
    new Action(2441, 797, false, power, "TEST"),
    new Action(-1745, 1732, false, power, "TEST"),
    new Action(-497, -2390, false, power, "TEST")
  };
  refereeCopy.assignActions(1, actions1);

  vector<Action*> actions2 = {
    new Action(-881, -2405, false, power, "TEST"),
    new Action(-1330, 2149, false, power, "TEST"),
    new Action(1128, -702, false, power, "TEST")
  };
  refereeCopy.assignActions(2, actions2);

  refereeCopy.updateGame();

  // depth 2
  vector<Action*> actions3 = {
    new Action(2285, 636, false, power, "TEST"),
    new Action(-1662, 1757, false, power, "TEST"),
    new Action(-633, -3123, false, power, "TEST")
  };
  refereeCopy.assignActions(1, actions3);

  vector<Action*> actions4 = {
    new Action(-894, -2128, false, power, "TEST"),
    new Action(-1314, 1947, false, power, "TEST"),
    new Action(1780, -594, false, power, "TEST")
  };
  refereeCopy.assignActions(2, actions4);

  refereeCopy.updateGame();

  // depth 3
  vector<Action*> actions5 = {
    new Action(2558, 341, false, power, "TEST"),
    new Action(-1689, 1779, false, power, "TEST"),
    new Action(-1496, -2617, false, power, "TEST")
  };
  refereeCopy.assignActions(1, actions5);

  vector<Action*> actions6 = {
    new Action(-703, -2636, false, power, "TEST"),
    new Action(-1490, 1923, false, power, "TEST"),
    new Action(1879, -223, false, power, "TEST")
  };
  refereeCopy.assignActions(2, actions6);

  refereeCopy.updateGame();

  cout << refereeCopy.toString();
}
