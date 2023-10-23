# TAN Network

## Problem Description

The goal of this puzzle is to create a program that calculates the shortest route between two public transportation stops in the Loire-Atlantique region in France, served by the TAN public transport company. The input data for this program includes a list of stops and the routes between them.

## Solution Summary

To solve this puzzle and find the optimal path between two stops, you can use a graph-based algorithm like Dijkstra's algorithm or A* search. Here are the steps to do it:

1. Parse the input data:
   - Read the list of stops, including their unique identifiers, full names, and coordinates.
   - Read the routes between the stops, representing one-directional connections between stops.

2. Create a graph:
   - Represent the stops as nodes in a graph.
   - Use the routes to create edges between the stops, considering both directions (A to B and B to A).

3. Implement Dijkstra's algorithm or A* search:
   - Initialize a priority queue or min-heap to keep track of the stops to explore.
   - Start with the initial stop as the source and add it to the queue with a distance of 0.
   - While the queue is not empty, repeat the following steps:
     - Pop the stop with the shortest distance from the queue.
     - For each neighboring stop connected by an edge, calculate the distance from the source to that neighbor.
     - If the newly calculated distance is shorter than the current recorded distance for that neighbor, update it.
     - Keep track of the previous stop for each neighbor to reconstruct the path later.

4. Determine the shortest path:
   - Once the algorithm reaches the destination stop, you can reconstruct the shortest path by backtracking from the destination to the source using the previous stop information.

5. Output the result:
   - If a path is found, display the full names of the stops along the shortest route.
   - If no path exists between the starting and final stops, display "IMPOSSIBLE."

This algorithm ensures that you find the shortest route between two stops in the TAN network, and it takes into account the provided stop information and routes.

## Run the tests

```shell
python3 puzzles/python3/tan-network/test_tan_network_a_star.py
```
