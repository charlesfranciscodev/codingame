# Skynet Revolution - Episode 1

The puzzle is implemented in Python 3 and the code can be found in the following GitHub repository: [Skynet Revolution 1](https://github.com/charlesfranciscodev/codingame/blob/master/puzzles/python3/skynet-revolution1)

## Problem Description

In the "Skynet Revolution 1" puzzle, you are tasked with disconnecting a computer virus called Skynet from its main server. Skynet is trying to escape and spread throughout the network, and your goal is to prevent this by severing the links between nodes in the network.

The network is represented as a graph where nodes are connected by edges. You can cut one edge per turn, and Skynet will move along the remaining edges to reach its destination. Your objective is to cut the edges in a way that maximizes the number of turns required for Skynet to reach its destination node.

The game consists of a series of rounds. In each round, you receive information about the network and the positions of Skynet and the exit node. You need to analyze the situation and determine which edge to cut.

## Solution

To solve the Skynet Revolution 1 puzzle, you can use the following approach:

1. Parse the input to obtain the network information.
2. Identify the links connected to Skynet's current position.
3. Check if any of the links are directly connected to the exit node. If yes, cut that link.
4. If there are no direct links to the exit node, cut any link connected to Skynet's current position.
5. Output the chosen edge to cut.

Here's an example implementation of the solution in Python:

```python
def bfs(graph, gateways, agentNodeId):
    visited = set()
    queue = []
    cameFrom = {}  # node id => parent node id on the shortest path
    queue.append(agentNodeId)
    visited.add(agentNodeId)

    while len(queue) != 0:
        nodeId = queue.pop(0)
        for neighborId in graph[nodeId]:
            if neighborId not in visited:
                visited.add(neighborId)
                queue.append(neighborId)
                cameFrom[neighborId] = nodeId
                if neighborId in gateways:
                    return cameFrom, neighborId

    return None, None

def reconstructPath(cameFrom, neighborId):
    currentId = neighborId
    stack = []

    while currentId in cameFrom:
        stack.append(currentId)
        currentId = cameFrom[currentId]
    stack.append(currentId)
    return stack


# read game input
graph = {}  # node id => links
gateways = set()
nbNodes, nbLinks, nbGateways = map(int, input().split())
for i in range(nbLinks):
    n1, n2 = map(int, input().split())
    if n1 not in graph:
        graph[n1] = set()
    if n2 not in graph:
        graph[n2] = set()
    graph[n1].add(n2)
    graph[n2].add(n1)
for i in range(nbGateways):
    gateways.add(int(input()))

# game loop
while True:
    agentNodeId = int(input())
    cameFrom, neighborId = bfs(graph, gateways, agentNodeId)
    if cameFrom is not None and neighborId is not None:
        path = reconstructPath(cameFrom, neighborId)
        secondNodeId = path[-2]
        graph[agentNodeId].remove(secondNodeId)
        graph[secondNodeId].remove(agentNodeId)

    # the indices of the nodes you wish to sever the link between
    print(f"{agentNodeId} {secondNodeId}")
```
