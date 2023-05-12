# Shadows of the Knight - Episode 1

This is a solution to the "Shadows of the Knight - Episode 1" puzzle on CodinGame.

## Problem Description

The problem requires us to simulate a scenario where Batman is trying to locate the Joker in a building with N floors and M rooms per floor. Batman starts at a certain position in the building and has a limited number of moves. In each move, he can choose to move up, down, left or right to a new position in the building. The building is described by a 2D grid of characters, where '.' represents an empty room, '#' represents a wall, and 'X' represents the location of the Joker.

The objective is to determine the location of the Joker using the fewest possible number of moves.

## Solution Overview

To solve the problem, we will use a binary search algorithm to determine the location of the Joker on each turn. The basic idea is to divide the building into smaller and smaller sub-regions by guessing the position of the Joker on each turn. We will start with a search space that includes the entire building, and then refine our search space on each turn based on the feedback provided by Batman's movements.

## Conclusion

The "Shadows of the Knight - Episode 1" puzzle is a simple example of a search problem that can be solved using a binary search algorithm. The solution presented here demonstrates the basic concepts involved in solving such problems and can be used as a starting point for more complex search problems.
