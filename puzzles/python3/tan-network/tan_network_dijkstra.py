import math
from collections import defaultdict
from typing import Dict, List, Set


class Node:
    EARTH_RADIUS = 6371

    def __init__(self, node_id: str, full_name: str, latitude: str, longitude: str):
        self.node_id = node_id
        self.full_name = full_name.replace('"', "")
        self.latitude = math.radians(float(latitude))
        self.longitude = math.radians(float(longitude))
        self.edges = []

    def distance(self, other) -> float:
        x = (other.longitude - self.longitude) * math.cos((self.latitude + other.latitude) / 2)
        y = other.latitude - self.latitude
        return math.hypot(x, y) * self.EARTH_RADIUS


def closest_node(graph: Dict[str, Node], opened: Set[str], distances: Dict[str, float]) -> Node:
    min_node = None
    min_distance = math.inf
    for node_id in opened:
        node = graph[node_id]
        if distances[node.node_id] < min_distance:
            min_node = node
            min_distance = distances[node.node_id]
    return min_node


def explore_graph(graph: Dict[str, Node], start_id: str, end_id: str) -> Dict[str, str]:
    """Dijkstra's algorithm"""
    parents: Dict[str, str] = {}  # child id => parent id
    opened: Set[str] = set()  # nodes to explore
    distances: Dict[str, float] = defaultdict(lambda: math.inf)  # node id => distance from the start node
    distances[start_id] = 0
    opened.add(start_id)
    parents[start_id] = None

    for node_id in graph:
        opened.add(node_id)

    while opened:
        current_node = closest_node(graph, opened, distances)
        if not current_node:
            return None
        opened.remove(current_node.node_id)
        if current_node.node_id == end_id:
            return parents
        for neighbor_id in current_node.edges:
            neighbor_node = graph[neighbor_id]
            new_distance = distances[current_node.node_id] + current_node.distance(neighbor_node)
            if new_distance < distances[neighbor_id]:
                # found a better path
                distances[neighbor_id] = new_distance
                parents[neighbor_id] = current_node.node_id


def reconstruct_path(parents: Dict[str, str], end_id: str):
    if not parents:
        return []

    # build the path from the end
    stack = [end_id]
    current_id = end_id
    while current_id:
        current_id = parents[current_id]
        if current_id:
            stack.append(current_id)

    return stack


def print_path(graph: Dict[str, Node], stack: List[str]):
    # print the path
    if not stack:
        print("IMPOSSIBLE")
    while stack:
        node_id = stack.pop()
        print(graph[node_id].full_name)


if __name__ == "__main__":
    graph: Dict[str, Node] = {}
    start_id = input()
    end_id = input()

    n = int(input())
    for _ in range(n):
        node_id, full_name, _, latitude, longitude, _, _, _, _ = input().split(",")
        node = Node(node_id, full_name, latitude, longitude)
        graph[node_id] = node

    m = int(input())
    for _ in range(m):
        try:
            data = input()
            node_id_from, node_id_to = data.split(" ")
            graph[node_id_from].edges.append(node_id_to)
        except EOFError:
            break

    parents = explore_graph(graph, start_id, end_id)
    stack = reconstruct_path(parents, end_id)
    print_path(graph, stack)
