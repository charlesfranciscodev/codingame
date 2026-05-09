# Power of Thor - Episode 1

## Description

In this puzzle, Thor is stranded on a rectangular grid and needs to reach a lightning bolt that is located at a specific position on the grid. The position of Thor and the lightning bolt are given as input to the program. Thor can move in four directions: North, South, East, and West. For each move, the program needs to output the direction in which Thor should move to get closer to the lightning bolt.

## Solution Overview

The solution uses a loop to iterate over the possible moves of Thor. At each iteration, the program calculates the direction in which Thor should move based on his current position and the position of the lightning bolt. The program then outputs the direction in which Thor should move and updates his position accordingly.

## Example Input/Output

**Initialization input**

```
31 4 5 4
```

**Output for a game round**

```
E
```

## Code Example

```python
light_x, light_y, thor_x, thor_y = map(int, input().split())

while True:
    remaining_turns = int(input())
    
    direction = ""

    # Determine the vertical direction (N or S) and update position
    if thor_y > light_y:
        direction += "N"
        thor_y -= 1
    elif thor_y < light_y:
        direction += "S"
        thor_y += 1

    # Determine the horizontal direction (E or W) and update position
    if thor_x > light_x:
        direction += "W"
        thor_x -= 1
    elif thor_x < light_x:
        direction += "E"
        thor_x += 1

    print(direction)
```
