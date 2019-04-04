from collections import deque
from typing import Deque, Dict, List


LAND = '#'
WATER = 'O'
DEFAULT_INDEX = -1


class Node:
    def __init__(self, x: int, y: int, terrain: str):
        self.x = x
        self.y = y
        self.terrain = terrain
        self.lake_index = DEFAULT_INDEX


class Grid:
    def __init__(self):
        self.width = 0
        self.height = 0
        self.nodes: List[List[Node]] = []
        self.lakes: Dict[int, int] = {}  # lake_index: surface area

    def read_game_input(self):
        self.width = int(input())
        self.height = int(input())
        for y in range(self.height):
            row: List[Node] = [Node(x, y, terrain) for x, terrain in enumerate(input())]
            self.nodes.append(row)

    def test(self):
        nb_coordinates = int(input())
        for _ in range(nb_coordinates):
            x, y = map(int, input().split())
            print(self.area(x, y))

    def area(self, x: int, y: int) -> int:
        node = self.nodes[y][x]
        if node.terrain == LAND:
            return 0
        if node.lake_index == DEFAULT_INDEX:
            self.flood_fill(node)
        return self.lakes[node.lake_index]

    def flood_fill(self, start: Node):
        queue: Deque[Node] = deque()
        total_area = 0
        start.lake_index = start.y * self.width + start.x
        queue.append(start)

        while len(queue) != 0:
            total_area += 1
            current_node = queue.popleft()
            self.fill_neighbors(queue, current_node, start.lake_index)
        self.lakes[start.lake_index] = total_area

    def fill_neighbors(self, queue, node, lake_index):
        if node.x + 1 < self.width:
            right_neighbor = self.nodes[node.y][node.x + 1]
            self.fill(queue, right_neighbor, lake_index)

        if node.x > 0:
            left_neighbor = self.nodes[node.y][node.x - 1]
            self.fill(queue, left_neighbor, lake_index)

        if node.y + 1 < self.height:
            down_neighbor = self.nodes[node.y + 1][node.x]
            self.fill(queue, down_neighbor, lake_index)

        if node.y > 0:
            up_neighbor = self.nodes[node.y - 1][node.x]
            self.fill(queue, up_neighbor, lake_index)

    def fill(self, queue: Deque[Node], node: Node, lake_index: int):
        if node.terrain == WATER and node.lake_index == DEFAULT_INDEX:
            node.lake_index = lake_index
            queue.append(node)


if __name__ == "__main__":
    grid = Grid()
    grid.read_game_input()
    grid.test()
