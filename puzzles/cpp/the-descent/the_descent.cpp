#include <iostream>
using namespace std;

int main() {
    // Game loop
    while (true) {
        int highestIndex = 0;
        int highestHeight = -1;

        // Read the heights of the mountains and determine the highest
        for (int i = 0; i < 8; i++) {
            int mountainHeight;
            cin >> mountainHeight;

            // Check if this mountain is the highest so far
            if (mountainHeight > highestHeight) {
                highestHeight = mountainHeight;
                highestIndex = i;
            }
        }

        // Output the index of the highest mountain to shoot
        cout << highestIndex << endl;
    }
}
