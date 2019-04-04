from typing import Dict, Set


class Node:
    def __init__(self):
        self.children: Set[int] = set()
        self.depth = 0


class Graph:
    def __init__(self):
        self.nodes: Dict[int, Node] = {}  # node_id => node

    def build(self):
        nb_edges = int(input())  # the number of relationships of influence
        for _ in range(nb_edges):
            parent_id, child_id = map(int, input().split())

            if child_id in self.nodes:
                child: Node = self.nodes[child_id]
            else:
                child: Node = Node()
                self.nodes[child_id] = child

            if parent_id in self.nodes:
                parent: Node = self.nodes[parent_id]
                parent.children.add(child_id)
            else:
                parent: Node = Node()
                parent.children.add(child_id)
                self.nodes[parent_id] = parent

    def solve(self) -> int:
        """Returns the number of people involved in the longest succession of influences."""
        max_depth = 0
        for node in self.nodes.values():
            self.traverse(node)
        for node in self.nodes.values():
            if node.depth > max_depth:
                max_depth = node.depth
        return max_depth + 1

    def traverse(self, node: Node):
        for child_id in node.children:
            child: Node = self.nodes[child_id]
            if child.depth <= node.depth:
                child.depth = node.depth + 1
                self.traverse(child)


if __name__ == "__main__":
    graph = Graph()
    graph.build()
    print(graph.solve())
