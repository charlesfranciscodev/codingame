Here's a possible solution to the "Onboarding" challenge on CodinGame using C++:

```c++
#include <iostream>
#include <string>

using namespace std;

int main()
{
    while (true) {
        string enemy1;
        int dist1;
        string enemy2;
        int dist2;

        cin >> enemy1 >> dist1 >> enemy2 >> dist2;

        // Determine which enemy is closer and print its name
        if (dist1 < dist2) {
            cout << enemy1 << endl;
        } else {
            cout << enemy2 << endl;
        }
    }

    return 0;
}
```

In this solution, we use a `while` loop to continuously read input from the standard input until the program is terminated. In each iteration of the loop, we read the name and distance of two enemies using `cin`, and then determine which one is closer based on their distances. Finally, we print the name of the closer enemy using `cout`. Note that we use `endl` to add a newline character at the end of each output line.