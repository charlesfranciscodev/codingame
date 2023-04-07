# Surface

The coding challenge on the website https://www.codingame.com/training/hard/surface asks the user to write a program that calculates the total surface area of a group of connected cells in a two-dimensional grid. The grid consists of cells that are either black or white, and the cells are connected horizontally or vertically. The program must read the input which contains the dimensions of the grid and the color of each cell, and then output the total surface area of the largest group of connected cells of the same color.

To solve this challenge, the program must use a graph traversal algorithm, such as depth-first search or breadth-first search, to find the connected components of cells that have the same color. Once the program has identified all of the connected components, it can calculate the surface area of each component and return the maximum surface area.

The program needs to handle different edge cases, such as a grid that has only black cells or only white cells, a grid with only one cell, or a grid with disconnected components of the same color. The challenge also provides multiple test cases to ensure that the program correctly handles various inputs.
