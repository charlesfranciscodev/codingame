# The Descent Puzzle

## Description

The goal of the puzzle is to destroy the mountains by firing at the highest one at the start of each game turn. The heights of the mountains are given as input, and the output should be the index of the mountain to fire at. The game is won if all the mountains are destroyed, and lost if the ship crashes into a mountain.

## Algorithm

The following code snippet is a game loop that continuously reads the heights of 8 mountains and outputs the index of the highest mountain to "shoot" at. It does this by iterating through the mountain heights, keeping track of the highest height and its corresponding index, and then printing the index of the highest mountain. The loop repeats indefinitely.

## Example Input/Output

**Input for one game turn**

```
9
8
7
6
5
4
3
2
```

**Output for one game turn**

```
0
```

## Code Example

```python
while True:
    highest_index = 0
    highest_height = -1

    # Read the heights of the mountains and determine the highest
    for i in range(8):
        mountain_height = int(input())
        
        # Check if this mountain is the highest so far
        if mountain_height > highest_height:
            highest_height = mountain_height
            highest_index = i

    # Output the index of the highest mountain to shoot
    print(highest_index)
```
