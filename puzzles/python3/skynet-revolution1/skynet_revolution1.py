from collections import deque
from typing import Deque, Dict, Optional, List, Set, Tuple


def bfs(
    graph: Dict[int, Set[int]],
    gateways: Set[int],
    agent_node_id: int
) -> Tuple[Optional[Dict[int, int]], Optional[int]]:
    visited = set()
    queue: Deque[int] = deque()
    came_from: Dict[int, int] = {}  # node id => parent node id on the shortest path
    queue.append(agent_node_id)
    visited.add(agent_node_id)

    while queue:
        node_id = queue.popleft()
        for neighbor_id in graph[node_id]:
            if neighbor_id not in visited:
                visited.add(neighbor_id)
                queue.append(neighbor_id)
                came_from[neighbor_id] = node_id
                if neighbor_id in gateways:
                    return (came_from, neighbor_id)

    return (None, None)


def reconstruct_path(came_from: Dict[int, int], neighbor_id: int) -> List[int]:
    current_id: int = neighbor_id
    stack: List[int] = []

    while current_id in came_from:
        stack.append(current_id)
        current_id = came_from[current_id]
    stack.append(current_id)
    return stack


if __name__ == "__main__":
    # read game input
    graph: Dict[int, Set[int]] = {}  # node id => links
    gateways: Set[int] = set()
    nb_nodes, nb_links, nb_gateways = map(int, input().split())
    for i in range(nb_links):
        # n1 and n2 defines a link between these nodes
        n1, n2 = map(int, input().split())
        if n1 not in graph:
            graph[n1] = set()
        if n2 not in graph:
            graph[n2] = set()
        graph[n1].add(n2)
        graph[n2].add(n1)
    for i in range(nb_gateways):
        gateways.add(int(input()))

    # game loop
    while True:
        agent_node_id = int(input())  # node id on which the Skynet agent is located
        came_from, neighbor_id = bfs(graph, gateways, agent_node_id)
        if came_from is not None and neighbor_id is not None:
            path: List[int] = reconstruct_path(came_from, neighbor_id)
            second_node_id = path[-2]
            graph[agent_node_id].remove(second_node_id)
            graph[second_node_id].remove(agent_node_id)
            # the indices of the nodes you wish to sever the link between
            print(f"{agent_node_id} {second_node_id}")
