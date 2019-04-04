#include <iostream>
#include <cmath>

using namespace std;

int main() {
  int n; // the number of temperatures to analyse
  cin >> n; cin.ignore();
  int minT = 5526;
  for (int i = 0; i < n; i++) {
    int t; // a temperature expressed as an integer ranging from -273 to 5526
    cin >> t; cin.ignore();
    if (abs(t) < abs(minT) || abs(t) == abs(minT) && t > minT) {
      minT = t;
    }
  }

  if (n == 0) {
    cout << 0 << endl;
  } else {
    cout << minT << endl;
  }
}
