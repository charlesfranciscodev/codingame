import math
from collections import defaultdict


def read_game_input():
    nodes = defaultdict(list)  # node_id => [(neighbor_id, distance)]
    h_values = {}

    nb_nodes, nb_edges, start_id, goal_id = map(int, input().split())
    for node_id, i in enumerate(input().split()):
        h_value = int(i)
        h_values[node_id] = h_value

    for i in range(nb_edges):
        node_id_x, node_id_y, distance = map(int, input().split())
        nodes[node_id_x].append((node_id_y, distance))
        nodes[node_id_y].append((node_id_x, distance))

    return nb_nodes, nodes, h_values, start_id, goal_id


def a_star(nodes, h_values, start_id, goal_id):
    closed_set = set()
    open_set = {start_id}
    g_values = defaultdict(lambda: math.inf)
    f_values = defaultdict(lambda: math.inf)
    g_values[start_id] = 0
    f_values[start_id] = h_values[start_id]

    while len(open_set) != 0:
        current_id = minimum(open_set, f_values)
        print(f"{current_id} {f_values[current_id]}")
        if current_id == goal_id:
            return
        open_set.remove(current_id)
        closed_set.add(current_id)

        for neighbor_id, distance in nodes[current_id]:
            if neighbor_id in closed_set:
                continue
            g_value = g_values[current_id] + distance
            if neighbor_id not in open_set:
                open_set.add(neighbor_id)
            elif g_value >= g_values[neighbor_id]:
                continue
            g_values[neighbor_id] = g_value
            f_values[neighbor_id] = g_value + h_values[neighbor_id]


def minimum(open_set, f_values):
    """Compute the node_id in open_set with the minimum f_value"""
    min_id = None
    min_f_value = math.inf
    for identifier in open_set:
        f_value = f_values[identifier]
        if f_value < min_f_value:
            min_id = identifier
            min_f_value = f_value
    return min_id


if __name__ == "__main__":
    nb_nodes, nodes, h_values, start_id, goal_id = read_game_input()
    a_star(nodes, h_values, start_id, goal_id)
