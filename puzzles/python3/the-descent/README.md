# The Descent Puzzle

## Description

In "The Descent" puzzle, you are given an array of integers representing the heights of a set of mountains. Your goal is to determine which mountain is the tallest and shoot it down by printing its index to the console.

## Approach

The approach for solving "The Descent" puzzle is simple. You iterate over the array of mountains and keep track of the tallest mountain seen so far. Once you have iterated over all the mountains, you print the index of the tallest mountain to the console.

## Example Input/Output

Let's consider the following array of mountains:

```
[9, 8, 6, 7, 3, 5, 4, 1, 2]
```

Here, the tallest mountain is the one with a height of `9`. The index of this mountain in the array is `0`. Therefore, the output of the program should be:

```
0
```

## Code Example

```python
import sys

# Game loop
while True:
    heights = []
    
    # Read the heights of the mountains
    for _ in range(8):
        mountain_height = int(input())  # Height of the mountain
        heights.append(mountain_height)
    
    # Find the index of the highest mountain
    max_height = max(heights)
    max_height_index = heights.index(max_height)
    
    # Output the index of the highest mountain to shoot
    print(max_height_index)

```
