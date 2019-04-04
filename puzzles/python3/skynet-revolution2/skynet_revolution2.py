from collections import deque
from typing import Deque, List


class Node:
    def __init__(self, index: int):
        self.index = index
        self.links: List[Node] = []
        self.is_gateway = False
        self.is_marked = False

    @property
    def nb_gateway_links(self) -> int:
        return sum(link.is_gateway for link in self.links)

    def get_gateway_link(self):
        return next((link for link in self.links if link.is_gateway), None)


class Graph:
    def __init__(self):
        self.nodes: List[Node] = []
        self.target_gateways: List[Node] = []

    def update_targets(self, gateway: Node):
        if not gateway.links:
            self.target_gateways.remove(gateway)

    def reset(self):
        for node in self.nodes:
            node.is_marked = False

    def sever(self, node1: Node, node2: Node):
        """sever the link between the nodes n1 and n2"""
        print(f"{node1.index} {node2.index}")

    def read_init_input(self):
        self.nb_nodes, nb_links, self.nb_gateways = map(int, input().split())

        for index in range(self.nb_nodes):
            self.nodes.append(Node(index))

        for _ in range(nb_links):
            # n1 and n2 defines a link between these nodes
            n1, n2 = map(int, input().split())
            node1: Node = self.nodes[n1]
            node2: Node = self.nodes[n2]
            node1.links.append(node2)
            node2.links.append(node1)

        for _ in range(self.nb_gateways):
            index = int(input())  # index of a gateway node
            gateway = self.nodes[index]
            gateway.is_gateway = True
            self.target_gateways.append(gateway)

    def game_loop(self):
        while True:
            # The node on which the Skynet agent is positioned this turn
            agent_index = int(input())
            if not self.block_nearby_agent(agent_index):
                if not self.block_double_gateway(agent_index):
                    self.block_gateway()

    def block_nearby_agent(self, agent_index: int) -> bool:
        """If the agent is linked to an exit, sever the link and return True. Otherwise, return False"""
        agent_node: Node = self.nodes[agent_index]
        for node in agent_node.links:
            if node.is_gateway:
                self.sever(agent_node, node)
                agent_node.links.remove(node)
                node.links.remove(agent_node)
                self.update_targets(node)
                return True
        return False

    def block_double_gateway(self, agent_index: int) -> bool:
        """
        Slice the last link on the shortest path between the virus and a gateway using BFS.
        Only danger nodes are considered in possible paths. A danger node is a node with 1 or more gateway links.
        The link is severed if the node is linked to 2 gateways.
        """
        agent_node = self.nodes[agent_index]
        queue: Deque[Node] = deque()
        self.reset()
        agent_node.is_marked = True
        queue.append(agent_node)

        while queue:
            current_node: Node = queue.popleft()
            for neighbor in current_node.links:
                nb_gateway_links = neighbor.nb_gateway_links
                if not neighbor.is_gateway and nb_gateway_links >= 1 and not neighbor.is_marked:
                    neighbor.is_marked = True
                    if nb_gateway_links == 2:
                        gateway = neighbor.get_gateway_link()
                        self.sever(neighbor, gateway)
                        neighbor.links.remove(gateway)
                        gateway.links.remove(neighbor)
                        self.update_targets(gateway)
                        return True
                    else:
                        queue.append(neighbor)
        return False

    def block_gateway(self):
        """Slice a gateway link."""
        gateway = self.target_gateways[0]
        node = gateway.links[0]
        self.sever(gateway, node)
        gateway.links.remove(node)
        node.links.remove(gateway)
        self.update_targets(gateway)


if __name__ == "__main__":
    graph = Graph()
    graph.read_init_input()
    graph.game_loop()
