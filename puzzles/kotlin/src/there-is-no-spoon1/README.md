Sure, here's the Markdown document for the "There Is No Spoon 1" coding puzzle in Kotlin without the code section:

# There Is No Spoon 1 - Kotlin Solution

This is a solution in Kotlin to the "There Is No Spoon 1" coding puzzle on [CodinGame](https://www.codingame.com/training/easy/there-is-no-spoon-episode-1).

## Problem Description

The problem requires finding the neighboring cells of each node in a 2D grid with no space between cells. The cells are represented by "." in the input string, and the node indices are represented by "0". The output is the indices of the neighboring nodes for each node.

## Solution

The solution reads the input grid into a 2D array of characters, and then iterates over the cells to find the neighboring cells. The neighboring cells are found by searching in each direction from the current cell until the edge of the grid is reached or another node is found.

The solution uses a nested loop to iterate over the cells, and then a nested loop to search in each direction for neighboring cells. The indices of neighboring nodes are stored in a list, and then output at the end of the search for each node.