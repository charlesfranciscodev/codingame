# Tan Network

This is a solution for the "Tan Network" puzzle on Codingame platform, written in Kotlin.

## Problem Description

The problem statement can be found on the following link: https://www.codingame.com/training/medium/tan-network

In summary, the problem is about finding the shortest path between two nodes in a weighted graph.

## Solution

The solution to this problem is based on Dijkstra's algorithm. The basic idea is to start with a source node and then explore its neighboring nodes. We keep track of the distance from the source node to each neighboring node, and we update it if we find a shorter path. We then select the unexplored node with the shortest distance and repeat the process until we reach the target node.

The implementation involves a priority queue to select the next node to explore. The distance from the source node to each node is stored in an array. We also keep track of the visited nodes to avoid revisiting them.
