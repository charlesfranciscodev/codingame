# Blunder - Episode 2

## Problem Description

Blunder, a robot with a passion for money, has lost his sense of humor and fun due to a malfunction in his circuits. To restore his original behavior, you need to write a program that guides him to collect the maximum amount of money possible from a building. Blunder can detect bank notes from a distance and must navigate through rooms in the building to accumulate wealth.

Here are the rules and details of the problem:

### Rules

- Blunder is placed at the entrance of a building, which consists of multiple rooms.
- Each room contains a sum of money.
- Each room has exactly two doors, leading either to a new room or to the outside of the building.
- Blunder cannot backtrack through the same room.
- Blunder can analyze the building's layout and the money in each room using his sensors.
- Your program will receive input detailing the rooms, their money, and door connections.
- Your task is to create an algorithm that guides Blunder to collect the most money and exit the building.

### Input

- Line 1: An integer N, representing the number of rooms in the building.
- The following N lines each contain the following information about a room:
  - Room number (integer)
  - Sum of money in the room (integer)
  - Two numbers indicating the rooms accessible through doors (integers or "E" for outside exit)

### Output

- An integer representing the maximum amount of money that Blunder can collect by selecting a series of doors to reach the outside of the building.

### Constraints

- 0 < N < 10000

## Example

### Input

```
15
0 17 1 2
1 15 3 4
2 15 4 5
3 20 6 7
4 12 7 8
5 11 8 9
6 18 10 11
7 19 11 12
8 12 12 13
9 11 13 14
10 13 E E
11 14 E E
12 17 E E
13 19 E E
14 15 E E
```

### Output

```
88
```

## Solution Summary

You need to develop an algorithm to maximize the money Blunder can collect while navigating through the building. This problem can be solved using dynamic programming.

1. Create a list to store the maximum money Blunder can collect for each room.
2. Initialize the list with zeros for all rooms.
3. Start from the room at the entrance (room 0) and work your way through the building.
4. For each room, consider the two possible doors (or outside exit) to move to the next room.
5. Update the maximum money Blunder can collect for the current room by adding the money in the current room to the maximum money from the next room.
6. Continue this process for all rooms, ensuring that Blunder cannot revisit a room.
7. Finally, the maximum money Blunder can collect will be in the room with the outside exit.

Implement this algorithm to calculate the maximum money Blunder can collect and return it as the output.
