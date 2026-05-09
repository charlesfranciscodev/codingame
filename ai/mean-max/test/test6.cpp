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
    new Action(1151, -3634, false, power, "TEST"),
    new Action(1999, -1120, false, power, "TEST"),
    new Action(642, -2672, false, power, "TEST")
  };
  refereeCopy.assignActions(1, actions1);

  vector<Action*> actions2 = {
    new Action(1551, -2447, "TEST"),
    new Action(1248, -2968, false, power, "TEST"),
    new Action(891, -1306, false, power, "TEST")
  };
  refereeCopy.assignActions(2, actions2);

  refereeCopy.updateGame();

  cout << refereeCopy.toString();
}
