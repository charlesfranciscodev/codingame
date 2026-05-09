# Onboarding Puzzle

## Description

In this problem, you need to choose which enemy to shoot based on their distance from your ship. You can compare the distances of the two enemies and then shoot at the closest one.

## Algorithm

The solution uses a `while` loop to continuously read input from the standard input until the program is terminated. In each iteration of the loop, we read in the name and distance of two enemies using the `input()` function, and then compare their distances using an `if` statement. If the distance of the first enemy is less than the distance of the second enemy, we print the name of the first enemy. Otherwise, we print the name of the second enemy.

## Example Input/Output

**Input**

```
Nobody
Rock
9999
70
```

**Output**

```
Rock
```

## Code Example

The following code example provides a solution to the Onboarding puzzle. It reads input from the standard input, compares the distances of two enemies, and prints the name of the closest enemy to the standard output.

```python
import sys
import math

# game loop
while True:
    enemy_1 = input()  # name of enemy 1
    dist_1 = int(input())  # distance to enemy 1
    enemy_2 = input()  # name of enemy 2
    dist_2 = int(input())  # distance to enemy 2

    # Compare the distances of the two enemies
    if dist_1 < dist_2:
        # If enemy 1 is closer, shoot enemy 1
        print(enemy_1)
    else:
        # If enemy 2 is closer or at the same distance, shoot enemy 2
        print(enemy_2)

```
