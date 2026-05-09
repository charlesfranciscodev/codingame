import os
import unittest
from typing import Dict, List, Optional, Tuple

from tan_network_a_star import parse_game_input, traverse_with_a_star, generate_solution


def read_game_input_from_file(file_path: str) -> Tuple[str, str, List[str], List[str]]:
    with open(file_path) as reader:
        start_id = reader.readline().rstrip()
        end_id = reader.readline().rstrip()
        n = int(reader.readline().rstrip())
        input_lines_nodes: List[str] = []
        for _ in range(n):
            input_lines_nodes.append(reader.readline().rstrip())
        m = int(reader.readline().rstrip())
        input_lines_edges: List[str] = []
        for _ in range(m):
            input_lines_edges.append(reader.readline().rstrip())
    return start_id, end_id, input_lines_nodes, input_lines_edges


def read_solution_from_file(file_path: str) -> str:
    with open(file_path, "r") as reader:
        return "".join(reader)


def test_tan_network(file_name: str) -> Tuple[str, str]:
    input_file_path = os.path.join("./puzzles/python3/tan-network/test-input", file_name)
    start_id, end_id, input_lines_nodes, input_lines_edges = read_game_input_from_file(input_file_path)
    graph = parse_game_input(start_id, end_id, input_lines_nodes, input_lines_edges)
    came_from: Optional[Dict[str, str]] = traverse_with_a_star(graph)
    actual = generate_solution(graph, came_from)
    output_file_path = os.path.join("./puzzles/python3/tan-network/solution", file_name)
    expected = read_solution_from_file(output_file_path)
    return actual, expected


class TestTanNetworkAStar(unittest.TestCase):
    def test_example(self):
        actual, expected = test_tan_network("example.txt")
        self.assertEqual(actual, expected)

    def test_one_single_stop(self):
        actual, expected = test_tan_network("one-single-stop.txt")
        self.assertEqual(actual, expected)

    def test_same_start_and_end_points(self):
        actual, expected = test_tan_network("same-start-end.txt")
        self.assertEqual(actual, expected)

    def test_several_stages(self):
        actual, expected = test_tan_network("several-stages.txt")
        self.assertEqual(actual, expected)

    def test_large_nb_stages(self):
        actual, expected = test_tan_network("large-nb-stages.txt")
        self.assertEqual(actual, expected)

    def test_route_impossible(self):
        actual, expected = test_tan_network("impossible.txt")
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
