#include <iostream>
#include <algorithm>

using namespace std;

int main() {
  int width;
  cin >> width; cin.ignore();
  int height;
  cin >> height; cin.ignore();
  string text;
  getline(cin, text);
  transform(text.begin(), text.end(), text.begin(), ::toupper);
  for (int i = 0; i < height; i++) {
    string row;
    getline(cin, row);
    string output;
    for (char c : text) {
      int position = (int) (c - 'A');
      if (position < 0 || position > 25) {
        position = 26;
      }
      int start = position * width;
      output += row.substr(start, width);
    }
    cout << output << endl;
  }
}
