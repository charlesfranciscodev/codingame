import sys


def calculate_distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def find_nearest_neighbor(current_node, unvisited_nodes, nodes):
    min_distance = sys.maxsize
    nearest_neighbor = None
    for node in unvisited_nodes:
        distance = calculate_distance(nodes[current_node][0], nodes[current_node][1], nodes[node][0], nodes[node][1])
        if distance < min_distance:
            min_distance = distance
            nearest_neighbor = node
    return nearest_neighbor


def tsp_solver(nodes):
    num_nodes = len(nodes)
    unvisited_nodes = set(range(1, num_nodes))
    current_node = 0
    tsp_path = [current_node]

    while unvisited_nodes:
        nearest_neighbor = find_nearest_neighbor(current_node, unvisited_nodes, nodes)
        tsp_path.append(nearest_neighbor)
        unvisited_nodes.remove(nearest_neighbor)
        current_node = nearest_neighbor

    tsp_path.append(0)
    return tsp_path


# Read input
N = int(input())
nodes = []
for _ in range(N):
    x, y = map(int, input().split())
    nodes.append((x, y))

# Solve TSP
tsp_path = tsp_solver(nodes)

# Print output
print(' '.join(map(str, tsp_path)))
