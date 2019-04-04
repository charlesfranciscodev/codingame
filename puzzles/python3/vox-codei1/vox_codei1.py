import copy
from typing import List, Optional

EMPTY = '.'
TARGET = '@'
WALL = '#'
EXPLOSION_TIME = 3
BOMB_RANGE = 3


class Node:
    def __init__(self, x: int, y: int, symbol: str):
        self.x = x
        self.y = y
        self.symbol = symbol
        self.to_destroy = False
        self.time_to_detonation = EXPLOSION_TIME
        self.invalid = False

    def is_valid_target(self) -> bool:
        return self.symbol == TARGET and not self.to_destroy

    def is_valid_future_bomb_placement(self) -> bool:
        return not self.invalid and (self.symbol == EMPTY or (self.symbol == TARGET and self.to_destroy))

    def update(self):
        if self.symbol == TARGET and self.to_destroy:
            self.time_to_detonation -= 1
            if self.time_to_detonation == 0:
                self.symbol = EMPTY


class Grid:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.nodes: List[List[Node]] = []

    def mark_as_to_destroy(self, x: int, y: int):
        self.nodes[y][x].to_destroy = True

    def is_valid_target(self, x: int, y: int) -> bool:
        return self.nodes[y][x].is_valid_target()

    def is_valid_future_bomb_placement(self, x: int, y: int) -> bool:
        return self.nodes[y][x].is_valid_future_bomb_placement()

    def is_cleared(self) -> bool:
        for y in range(self.height):
            for x in range(self.width):
                if self.nodes[y][x].symbol == TARGET:
                    return False
        return True

    def update(self):
        for y in range(self.height):
            for x in range(self.width):
                self.nodes[y][x].update()

    def pick_bomb_placement(self) -> Optional[Node]:
        """Greedy solution: pick the bomb placement with the maximum score."""
        max_score = 0
        max_node: Optional[Node] = None
        for y in range(self.height):
            for x in range(self.width):
                if self.is_valid_future_bomb_placement(x, y):
                    score = self.place_bomb_score(x, y)
                    if score > max_score:
                        max_score = score
                        max_node = self.nodes[y][x]
        return max_node

    def place_bomb(self, x: int, y: int):
        """
        Update the state of the grid according to the coordinates of the bomb.
        Precondition: The node at (x, y) should be a valid target.
        """
        # BOTTOM
        for i in range(y + 1, y + BOMB_RANGE + 1):
            if i >= self.height:
                break
            if self.is_valid_target(x, i):
                self.mark_as_to_destroy(x, i)
            elif self.nodes[i][x].symbol == WALL:
                break

        # TOP
        for j in range(y - 1, y - (BOMB_RANGE + 1), -1):
            if j < 0:
                break
            if self.is_valid_target(x, j):
                self.mark_as_to_destroy(x, j)
            elif self.nodes[j][x].symbol == WALL:
                break

        # RIGHT
        for k in range(x + 1, x + BOMB_RANGE + 1):
            if k >= self.width:
                break
            if self.is_valid_target(k, y):
                self.mark_as_to_destroy(k, y)
            elif self.nodes[y][k].symbol == WALL:
                break

        # LEFT
        for m in range(x - 1, x - (BOMB_RANGE + 1), -1):
            if m < 0:
                break
            if self.is_valid_target(m, y):
                self.mark_as_to_destroy(m, y)
            elif self.nodes[y][m].symbol == WALL:
                break

    def place_bomb_score(self, x: int, y: int) -> int:
        """
        Returns the score for placing a bomb at the (x, y) position.
        score = number of targets destroyed
        Precondition: The node at (x, y) should be a valid target.
        """
        score = 0

        # BOTTOM
        for i in range(y + 1, y + BOMB_RANGE + 1):
            if i >= self.height:
                break
            if self.is_valid_target(x, i):
                score += 1
            elif self.nodes[i][x].symbol == WALL:
                break

        # TOP
        for j in range(y - 1, y - (BOMB_RANGE + 1), -1):
            if j < 0:
                break
            if self.is_valid_target(x, j):
                score += 1
            elif self.nodes[j][x].symbol == WALL:
                break

        # RIGHT
        for k in range(x + 1, x + BOMB_RANGE + 1):
            if k >= self.width:
                break
            if self.is_valid_target(k, y):
                score += 1
            elif self.nodes[y][k].symbol == WALL:
                break

        # LEFT
        for m in range(x - 1, x - (BOMB_RANGE + 1), -1):
            if m < 0:
                break
            if self.is_valid_target(m, y):
                score += 1
            elif self.nodes[y][m].symbol == WALL:
                break

        return score


class VoxCodei:
    def __init__(self):
        self.grid: Optional[Grid] = None
        self.nb_rounds_left = 0  # number of rounds left before the end of the game
        self.nb_bombs_left = 0
        self.round = 1

    def read_init_input(self):
        width, height = map(int, input().split())
        self.grid = Grid(width, height)
        for y in range(height):
            map_row = input()
            row: List[Node] = []
            self.grid.nodes.append(row)
            for x, symbol in enumerate(map_row):
                self.grid.nodes[y].append(Node(x, y, symbol))

    def game_loop(self):
        while True:
            self.nb_rounds_left, self.nb_bombs_left = map(int, input().split())
            self.play_turn()
            self.round += 1

    def play_turn(self):
        node: Optional[Node] = self.grid.pick_bomb_placement()

        # simulate everything for the selected node, if it doesn't work out, backtrack
        if node is not None:
            if not self.simulate_turn(node.x, node.y):
                node.invalid = True
                node = self.grid.pick_bomb_placement()

        # validate bomb placement for next turn
        if node is None or node.symbol != EMPTY:
            print("WAIT")  # wait until it gets destroyed
        else:
            self.grid.place_bomb(node.x, node.y)
            print(f"{node.x} {node.y}")

        self.grid.update()

    def simulate_turn(self, x: int, y: int) -> bool:
        bombs = self.nb_bombs_left
        rounds = self.nb_rounds_left
        grid_copy: Optional[Grid] = copy.deepcopy(self.grid)
        if not grid_copy:
            return False

        current: Optional[Node] = grid_copy.nodes[y][x]

        while bombs != 0 and rounds != 0 and not grid_copy.is_cleared():
            if current is not None and current.symbol == EMPTY:
                grid_copy.place_bomb(current.x, current.y)
                bombs -= 1
            grid_copy.update()
            rounds -= 1
            current = grid_copy.pick_bomb_placement()

        while rounds != 0 and not grid_copy.is_cleared():
            grid_copy.update()
            rounds -= 1

        return grid_copy.is_cleared()


if __name__ == "__main__":
    vox_codei = VoxCodei()
    vox_codei.read_init_input()
    vox_codei.game_loop()
