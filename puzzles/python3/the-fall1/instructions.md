Your objective is to write a program capable of predicting the route Indy will take on his way down a tunnel. Indy is not in danger of getting trapped in this first mission.

The tunnel consists of a patchwork of square rooms of different types.
The tunnel's origin point (x = 0 and y = 0) is at the top left corner of the grid.

Upon entering a room, depending on the type of the room and Indy's entrance point he will exit the room through a specific point.

Type 0
This room type is not part of the tunnel per se as Indy cannot move across it.

Type 1
Indy's possible entrance points are (TOP, LEFT, RIGHT).
Indy's possible exit points are (BOTTOM).

Type 2
Indy's possible entrance points are (LEFT, RIGHT).
Indy's possible exit points are (LEFT, RIGHT).

Type 3
Indy's possible entrance points are (TOP).
Indy's possible exit points are (BOTTOM).

Type 4
Indy can only move from TOP to LEFT or move from RIGHT to BOTTOM.

Type 5
Indy can only move from TOP to RIGHT or move from LEFT to BOTTOM.
Indy's possible entrance points are (TOP, LEFT).
Indy's possible exit points are (BOTTOM, RIGHT).

Type 6 is equivalent to Type 2

Type 7
Indy's possible entrance points are (TOP, RIGHT).
Indy's possible exit points are (BOTTOM).

Type 8
Indy's possible entrance points are (LEFT, RIGHT).
Indy's possible exit points are (BOTTOM).

Type 9
Indy's possible entrance points are (TOP, LEFT).
Indy's possible exit points are (BOTTOM).

Type 10
Indy's possible entrance points are (TOP).
Indy's possible exit points are (LEFT).

Type 11
Indy's possible entrance points are (TOP).
Indy's possible exit points are (RIGHT).

Type 12
Indy's possible entrance points are (RIGHT).
Indy's possible exit points are (BOTTOM).

Type 13
Indy's possible entrance points are (LEFT).
Indy's possible exit points are (BOTTOM).

Indy is perpetually drawn downwards: he cannot leave a room through the top.

At the start of the game, you are given the map of the tunnel in the form of a rectangular grid of rooms. Each room is represented by its type.

For this first mission, you will familiarize yourself with the tunnel system, the rooms have all been arranged in such a way that Indy will have a safe continuous route between his starting point (top of the temple) and the exit area (bottom of the temple).

Each game turn:
You receive Indy's current position
Then you specify what Indy's position will be next turn.
Indy will then move from the current room to the next according to the shape of the current room.

Game Input
The program must first read the initialization data from standard input. Then, within an infinite loop, read the data from the standard input related to the current position of Indy and provide to the standard output the expected data.

Initialization input
Line 1: 2 space separated integers W H specifying the width and height of the grid.

Next H lines: each line represents a line in the grid and contains W space separated integers T. T specifies the type of the room.

Last line: ignore this

Input for one game turn
Line 1: XI YI POS
(XI, YI) two integers to indicate Indy's current position on the grid.
POS a single word indicating Indy's entrance point into the current room: TOP if Indy enters from above, LEFT if Indy enters from the left and RIGHT if Indy enters from the right.

Output for one game turn
A single line with 2 integers: X Y representing the (X, Y) coordinates of the room in which you believe Indy will be on the next turn.

Initialization input
2 4 (W H)
4 3 (T T)
12 10 (T T)
11 5 (T T)
2 3 (T T)
1 (EX)

Input for turn 1
1 0 TOP (XI YI POS)

Output for turn 1
1 1

Input for turn 2
1 1 TOP (XI YI POS)

Output for turn 2
0 1

And so on until Indy reaches the exit at (1, 3).
