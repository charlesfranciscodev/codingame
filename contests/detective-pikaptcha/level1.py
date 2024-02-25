PASSAGE = "0"
WALL = "#"


class Game:
    def __init__(self):
        self.rows = []

    def read_input(self):
        self.width, self.height = map(int, input().split())
        for _ in range(self.height):
            self.rows.append(input())

    def solve(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.rows[y][x] == WALL:
                    print(WALL, end="")
                else:
                    print(self.adjacent_passable_cells(x, y), end="")
            print()

    def adjacent_passable_cells(self, x, y):
        count = 0
        if y > 0 and self.rows[y - 1][x] == PASSAGE:
            count += 1
        if y < self.height - 1 and self.rows[y + 1][x] == PASSAGE:
            count += 1
        if x > 0 and self.rows[y][x - 1] == PASSAGE:
            count += 1
        if x < self.width - 1 and self.rows[y][x + 1] == PASSAGE:
            count += 1
        return count


if __name__ == "__main__":
    game = Game()
    game.read_input()
    game.solve()
