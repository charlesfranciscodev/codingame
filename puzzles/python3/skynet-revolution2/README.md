# Skynet Revolution - Episode 2

The objective of this puzzle is to block the path of the Skynet agent to prevent him from reaching an exit. In order to do this, we can follow a strategy of elimination.
Our first priority is to look for immediate threats (the agent is located right next to an exit).

Our second priority is to attack danger nodes. Only danger nodes are considered in possible paths. A danger node is a node with 1 or more gateway links. The link is severed if the node is linked to 2 gateways. This is done to prevent the agent from chaining between danger nodes until it reaches a double gateway node. The goal is to slice the last link on the shortest path between the virus and a gateway using <a href="https://en.wikipedia.org/wiki/Breadth-first_search">BFS.</a>

Our last priority is to simply slice a random gateway link.
