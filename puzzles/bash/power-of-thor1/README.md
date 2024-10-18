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

```bash
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print thorX and thorY if Thor seems not to follow your orders.

# lightX: the X position of the light of power
# lightY: the Y position of the light of power
# thorX: Thor's current X position
# thorY: Thor's current Y position
read -r lightX lightY thorX thorY

# game loop
while true; do
    # remainingTurns: The remaining amount of turns Thor can move. Do not remove this line.
    read -r remainingTurns

    # Calculate the direction
    direction=""

    # Determine the vertical direction (N or S) and update position
    if [ "$thorY" -gt "$lightY" ]; then
        direction+="N"
        ((thorY--))
    elif [ "$thorY" -lt "$lightY" ]; then
        direction+="S"
        ((thorY++))
    fi

    # Determine the horizontal direction (E or W) and update position
    if [ "$thorX" -gt "$lightX" ]; then
        direction+="W"
        ((thorX--))
    elif [ "$thorX" -lt "$lightX" ]; then
        direction+="E"
        ((thorX++))
    fi

    # Output the direction
    echo "$direction"
done
```
