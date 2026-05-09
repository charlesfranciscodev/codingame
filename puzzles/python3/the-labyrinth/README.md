# The Labyrinth

## Summary

In this maze navigation problem, the goal is to guide Rick through an ASCII maze to deactivate a tracker beam at the control room and return to his starting position before an alarm goes off. Rick can move in four directions and has limited fuel. A BFS algorithm is used to explore the maze while keeping track of distance, fuel usage, and the alarm countdown. Success is achieved if Rick reaches the control room and returns to the starting position within the countdown, while failure occurs if he runs out of fuel, exceeds the countdown, or encounters walls or traps.

## Problem Description

You are tasked with guiding Rick, a fearless adventurer, through a treacherous maze in a mission to deactivate a tracker beam. The maze is represented in ASCII format and is composed of cells. Your goal is to safely navigate Rick through the maze, locate the control room (C), deactivate the tracker beam, and then return to the starting position (T) before an alarm countdown goes off. However, there are certain rules and limitations you must adhere to:

## Rules and Constraints

1. **Navigation**: Rick can move in four directions: UP, DOWN, LEFT, or RIGHT, as long as there are empty cells (represented by '.') in those directions.

2. **Scanning**: Rick's tricorder can only scan a 5-cell wide square centered on him. This means he can only see cells within a limited range.

3. **Fuel**: Rick's jetpack has enough fuel for 1200 movements. If he runs out of fuel, it's game over.

4. **Alarm Countdown**: Once Rick reaches the control room (C), an alarm countdown is triggered. You have a limited number of rounds to reach the starting position (T) before the alarm goes off. Failure to do so will result in Rick's demise.

5. **Traps**: Rick will die if he touches a wall ('#') or the ground ('#'), as there are mechanical traps in the maze.

## Input

You are given a maze in ASCII format as input. The maze contains the following characters:
- '#' represents a wall.
- '.' represents a hollow space.
- 'T' represents Rick's starting position.
- 'C' represents the control room.
- '?' represents a cell that Rick has not scanned yet.

Your task is to devise a plan to help Rick successfully accomplish his mission within these constraints.

## Solution Summary

To solve this maze-navigation puzzle and ensure Rick deactivates the tracker beam and returns safely to the starting position before the alarm goes off, we can employ a breadth-first search (BFS) algorithm. The BFS algorithm will help us explore the maze efficiently while keeping track of the alarm countdown and Rick's fuel usage.

Here's a step-by-step summary of the solution:

1. Initialize a queue for BFS traversal and a distance counter to keep track of how many movements Rick has made.

2. Start BFS from Rick's starting position (T).

3. Explore the maze using BFS, marking cells as visited and keeping track of distances.

4. While exploring, update Rick's fuel count and check for the following conditions:
   - If Rick reaches the control room (C), start the alarm countdown.
   - If Rick runs out of fuel, end the mission unsuccessfully.
   - If the alarm countdown reaches zero and Rick has not returned to the starting position, end the mission unsuccessfully.
   - If Rick encounters a wall or ground, end the mission unsuccessfully.

5. Continue BFS until either Rick successfully reaches the control room and returns to the starting position within the alarm countdown or one of the failure conditions is met.

6. If Rick succeeds in deactivating the tracker beam and returning to the starting position in time, the mission is a success.

The BFS algorithm guarantees that we explore the maze systematically, keeping track of the necessary parameters to ensure mission success. By following this plan, Rick can navigate the maze and accomplish his mission while avoiding potential traps and pitfalls.
