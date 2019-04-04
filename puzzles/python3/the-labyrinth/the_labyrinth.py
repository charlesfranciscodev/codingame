from collections import deque
from typing import Deque, Dict, List, Optional, Set, Tuple


Position = Tuple[int, int]

# Kirk's Possible Moves
UP = "UP"
DOWN = "DOWN"
LEFT = "LEFT"
RIGHT = "RIGHT"

# Possible ASCII Maze Characters
WALL = '#'
EMPTY = '.'
START = 'T'
CONTROL_ROOM = 'C'
UNKNOWN = '?'


class Game:
    def __init__(self, height: int, width: int):
        self.maze_explored = False
        self.control_room_reached = False
        self.height = height
        self.width = width
        self.maze: List[str] = []
        self.kirk_position: Position = (0, 0)  # (x, y)

    def loop(self):
        while True:
            kirk_y, kirk_x = map(int, input().split())
            self.kirk_position = (kirk_x, kirk_y)
            self.maze = []
            for y in range(height):
                row = input()
                self.maze.append(row)
                for x, c in enumerate(row):
                    if c == CONTROL_ROOM and (x, y) == self.kirk_position:
                        self.control_room_reached = True
            self.play()

    def play(self):
        came_from, neighbor = None, None
        if not self.maze_explored:
            to_avoid: Tuple[str] = (WALL, CONTROL_ROOM)
            came_from, neighbor = self.bfs(UNKNOWN, to_avoid)
            if not came_from:
                self.maze_explored = True
        if self.maze_explored:
            to_avoid: Tuple[str] = (WALL)
            if not self.control_room_reached:
                came_from, neighbor = self.bfs(CONTROL_ROOM, to_avoid)
            else:
                came_from, neighbor = self.bfs(START, to_avoid)

        path: List[Position] = self.reconstruct_path(came_from, neighbor)
        next_position = path[-2]
        self.print_next_move(next_position)

    def bfs(self, goal: str, to_avoid: Tuple[str]) -> Tuple[Optional[Dict[Position, Position]], Optional[Position]]:
        """Compute the shortest path between Kirk and the goal with BFS."""
        visited: Set[Position] = set()
        queue: Deque[Position] = deque()
        came_from: Dict[Position, Position] = {}  # position => parent position on the shortest path
        queue.append(self.kirk_position)
        visited.add(self.kirk_position)

        while len(queue) != 0:
            position: Position = queue.popleft()
            for neighbor in self.neighbors(position, to_avoid):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    came_from[neighbor] = position
                    neighbor_x, neighbor_y = neighbor
                    if self.maze[neighbor_y][neighbor_x] == goal:
                        return (came_from, neighbor)

        return (None, None)

    def neighbors(self, position: Position, to_avoid: Tuple[str]) -> List[Position]:
        neighbors: List[Position] = []
        x, y = position
        if x > 0:
            self.add_neighbor(to_avoid, neighbors, x - 1, y)
        if x < self.width - 1:
            self.add_neighbor(to_avoid, neighbors, x + 1, y)
        if y > 0:
            self.add_neighbor(to_avoid, neighbors, x, y - 1)
        if y < self.height - 1:
            self.add_neighbor(to_avoid, neighbors, x, y + 1)
        return neighbors

    def add_neighbor(self, to_avoid: Tuple[str], neighbors: List[Position], x, y):
        if self.maze[y][x] not in to_avoid:
            neighbors.append((x, y))

    def reconstruct_path(self, came_from: Dict[Position, Position], neighbor: Position) -> List[Position]:
        current_position: Position = neighbor
        stack: List[Position] = []
        while current_position in came_from:
            stack.append(current_position)
            current_position = came_from[current_position]
        stack.append(current_position)
        return stack

    def print_next_move(self, next_position: Position):
        kirk_x, kirk_y = self.kirk_position
        next_x, next_y = next_position
        if kirk_x < next_x:
            print(RIGHT)
        elif kirk_x > next_x:
            print(LEFT)
        elif kirk_y < next_y:
            print(DOWN)
        elif kirk_y > next_y:
            print(UP)


if __name__ == "__main__":
    height, width, _ = map(int, input().split())
    game = Game(height, width)
    game.loop()
