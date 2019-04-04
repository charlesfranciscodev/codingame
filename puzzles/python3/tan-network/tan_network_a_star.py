import math
from collections import defaultdict
from typing import Dict, List, Optional, Set, Tuple


class Node:
    EARTH_RADIUS = 6371

    def __init__(self, name: str, latitude: float, longitude: float):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.edges: List[str] = []

    def distance(self, other) -> float:
        x = (other.longitude - self.longitude) * math.cos((self.latitude + other.latitude) / 2)
        y = other.latitude - self.latitude
        return math.hypot(x, y) * self.EARTH_RADIUS


class Graph:
    def __init__(self, nodes: Dict[str, Node], start_id: str, end_id: str):
        self.nodes = nodes
        self.start_id = start_id
        self.end_id = end_id


def read_game_input() -> Tuple[str, str, List[str], List[str]]:
    start_id = input()
    end_id = input()
    n = int(input())
    input_lines_nodes: List[str] = []
    for _ in range(n):
        input_lines_nodes.append(input())
    m = int(input())
    input_lines_edges: List[str] = []
    for _ in range(m):
        input_lines_edges.append(input())
    return start_id, end_id, input_lines_nodes, input_lines_edges


def parse_game_input(start_id: str, end_id: str, input_lines_nodes: List[str], input_lines_edges: List[str]) -> Graph:
    nodes: Dict[str, Node] = {}
    for input_line in input_lines_nodes:
        data: List[str] = input_line.split(',')
        identifier = data[0]
        name = data[1].replace('\"', '')
        latitude = math.radians(float(data[3]))
        longitude = math.radians(float(data[4]))
        node = Node(name, latitude, longitude)
        nodes[identifier] = node

    for input_line in input_lines_edges:
        id_a, id_b = input_line.split()
        nodes[id_a].edges.append(id_b)

    return Graph(nodes, start_id, end_id)


def traverse_with_a_star(graph: Graph) -> Optional[Dict[str, str]]:
    """Compute the shortest path between start_id and end_id with the A* search algorithm."""
    closed_set: Set[str] = set()  # set of node ids already evaluated
    open_set: Set[str] = {graph.start_id}  # set of node ids to evaluate
    came_from: Dict[str, str] = {}  # child id => parent id on the shortest path
    g_scores: Dict[str, float] = defaultdict(lambda: math.inf)  # node_id => distance from the start
    f_scores: Dict[str, float] = defaultdict(lambda: math.inf)  # node_id => g_score + heuristic distance to the end
    g_scores[graph.start_id] = 0.0
    f_scores[graph.start_id] = graph.nodes[graph.start_id].distance(graph.nodes[graph.end_id])

    # loop until we reach the end or we run out of nodes to evaluate
    while open_set:
        current_id: Optional[str] = compute_minimum(open_set, f_scores)
        if current_id == graph.end_id:
            return came_from
        open_set.remove(current_id)
        closed_set.add(current_id)

        # explore neighbors
        for neighbor_id in graph.nodes[current_id].edges:
            if neighbor_id in closed_set:
                continue  # already evalutated this node
            neighbor_node = graph.nodes[neighbor_id]
            g_score = g_scores[current_id] + graph.nodes[current_id].distance(neighbor_node)
            if neighbor_id not in open_set:
                open_set.add(neighbor_id)  # first time we explore this node
            elif g_score >= g_scores[neighbor_id]:
                continue  # we already explored this node and the new distance is greater
            came_from[neighbor_id] = current_id
            g_scores[neighbor_id] = g_score
            f_scores[neighbor_id] = g_score + neighbor_node.distance(graph.nodes[graph.end_id])

    return None


def compute_minimum(open_set: Set[str], f_scores: Dict[str, float]) -> Optional[str]:
    """Compute the node_id in open_set with the minimum f_score"""
    min_id: Optional[str] = None
    min_f_score = math.inf
    for identifier in open_set:
        f_score = f_scores[identifier]
        if f_score < min_f_score:
            min_id = identifier
            min_f_score = f_score
    return min_id


def reconstruct_path(graph: Graph, came_from: Dict[str, str]) -> List[str]:
    current_id = graph.end_id
    stack: List[str] = []

    while current_id in came_from:
        stack.append(current_id)
        current_id = came_from[current_id]
    stack.append(current_id)
    return stack


def generate_solution(graph: Graph, came_from: Optional[Dict[str, str]]) -> str:
    if came_from is None:
        return "IMPOSSIBLE"
    else:
        node_names = []
        path: List[str] = reconstruct_path(graph, came_from)
        while path:
            node = graph.nodes[path.pop()]
            node_names.append(node.name)
        return '\n'.join(node_names)


if __name__ == "__main__":
    start_id, end_id, input_lines_nodes, input_lines_edges = read_game_input()
    graph = parse_game_input(start_id, end_id, input_lines_nodes, input_lines_edges)
    came_from: Optional[Dict[str, str]] = traverse_with_a_star(graph)
    solution = generate_solution(graph, came_from)
    print(solution)
