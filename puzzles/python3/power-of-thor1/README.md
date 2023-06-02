# Power of Thor

This is a solution to the Power of Thor puzzle on [Codingame](https://www.codingame.com/training/easy/power-of-thor-episode-1).

## Problem Description

In this puzzle, Thor is stranded on a rectangular grid and needs to reach a lightning bolt that is located at a specific position on the grid. The position of Thor and the lightning bolt are given as input to the program. Thor can move in four directions: North, South, East, and West. For each move, the program needs to output the direction in which Thor should move to get closer to the lightning bolt.

## Solution Overview

The solution uses a loop to iterate over the possible moves of Thor. At each iteration, the program calculates the direction in which Thor should move based on his current position and the position of the lightning bolt. The program then outputs the direction in which Thor should move and updates his position accordingly.

## Code Example

```python
# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    move = ""

    # Check the relative position of Thor and the light of power to determine the move direction
    if initial_ty > light_y:
        move += "N"
        initial_ty -= 1
    elif initial_ty < light_y:
        move += "S"
        initial_ty += 1

    if initial_tx > light_x:
        move += "W"
        initial_tx -= 1
    elif initial_tx < light_x:
        move += "E"
        initial_tx += 1

    print(move)

```

## Conclusion

This solution demonstrates how to solve the Power of Thor puzzle on Codingame. The program reads in input values from standard input, enters a loop to calculate the direction in which Thor should move, and outputs the direction in which he should move. This solution can be used as a starting point to solve other puzzles on Codingame or similar platforms.
