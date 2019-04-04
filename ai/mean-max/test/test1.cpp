#include <iostream>

#include "../../src/referee.cpp"

using namespace std;

int main() {
  Referee referee; 
  referee.readGameInfo();
  cout << referee.toString();
}
