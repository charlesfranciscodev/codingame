# Blunder - Episode 2

In this puzzle, you can implement a pathfinding algorithm, where the goal is not the shortest path but maximizing earnings. Here is one of the possible ways to solve this puzzle. Represent the bulding as a tree of rooms. Each room has a number, money, doors and depth in the tree. Calculate the maximum depth of each room reachable from the start with DFS. Find the path with the max total money using a modifed version of Dijkstra's algorithm, prioritizing the room with the highest depth.
