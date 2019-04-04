#include <iostream>

#include "../../src/referee.cpp"

using namespace std;

int main() {
  Referee referee;
  referee.readGameInfo();
  Referee refereeCopy(referee);

  vector<Action*> actions0 = {new Action(), new Action(), new Action()};
  refereeCopy.assignActions(0, actions0);

  int x = 0;
  int y = 0;
  int power = MAX_THRUST;

  vector<Action*> actions1 = {
    new Action(x, y, false, power, "TEST"),
    new Action(x, y, false, power, "TEST"),
    new Action(701, -5472, false, power, "TEST")
  };
  refereeCopy.assignActions(1, actions1);

  vector<Action*> actions2 = {
    new Action(x, y, false, power, "TEST"),
    new Action(x, y, false, power, "TEST"),
    new Action(4389, 3343, false, power, "TEST")
  };
  refereeCopy.assignActions(2, actions2);

  refereeCopy.updateGame();

  cout << refereeCopy.toString() << endl << endl;

  // test that original referee was not modified

  cout << referee.toString();
}
