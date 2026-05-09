#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
  vector<pair<int, int>> tasks;
  int n;
  cin >> n; cin.ignore();
  for (int i = 0; i < n; i++) {
    int startDay, duration;
    cin >> startDay >> duration; cin.ignore();
    pair<int, int> task = make_pair(startDay + duration - 1, startDay);
    tasks.push_back(task);
  }

  sort(tasks.begin(), tasks.end());

  vector<pair<int, int>> carryList;
  carryList.push_back(tasks[0]);
  int prevIndex = 0;
  for (int i = 0; i < n; i++) {
    pair<int, int> task = tasks[i];
    pair<int, int> prevTask = tasks[prevIndex];
    if (task.second > prevTask.first) {
      carryList.push_back(task);
      prevIndex = i;
    }
  }

  cout << carryList.size() << endl;
}
