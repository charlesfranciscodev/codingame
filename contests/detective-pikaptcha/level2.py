WALL = "#"

FOLLOW_RIGHT = "R"
FOLLOW_LEFT = "L"

RIGHT = ">"
DOWN = "v"
LEFT = "<"
UP = "^"

DIRECTIONS = {
    RIGHT,
    DOWN,
    LEFT,
    UP,
}

FOLLOW_RIGHT_PRIORITIES = {
    UP: [RIGHT, UP, LEFT, DOWN],
    DOWN: [LEFT, DOWN, RIGHT, UP],
    RIGHT: [DOWN, RIGHT, UP, LEFT],
    LEFT: [UP, LEFT, DOWN, RIGHT],
}

FOLLOW_LEFT_PRIORITIES = {
    UP: [LEFT, UP, RIGHT, DOWN],
    DOWN: [RIGHT, DOWN, LEFT, UP],
    RIGHT: [UP, RIGHT, DOWN, LEFT],
    LEFT: [DOWN, LEFT, UP, RIGHT],
}


class Pikachu:
    def __init__(self):
        self.start = (0, 0)
        self.previous = (0, 0)
        self.x = 0
        self.y = 0
        self.facing = ""
        self.priorities = {}

    def is_trapped(self):
        return self.previous == (self.x, self.y)


class Game:
    def __init__(self):
        self.rows = []
        self.width = 0
        self.height = 0
        self.pika = Pikachu()

    def read_input(self):
        self.width, self.height = map(int, input().split())
        for y in range(self.height):
            line = input()
            self.rows.append([])
            for x in range(self.width):
                if line[x] in DIRECTIONS:
                    self.pika.start = (x, y)
                    self.pika.x = x
                    self.pika.y = y
                    self.pika.facing = line[x]
                if line[x] == WALL:
                    self.rows[y].append(WALL)
                else:
                    self.rows[y].append(0)
        follow = input()
        if follow == FOLLOW_RIGHT:
            self.pika.priorities = FOLLOW_RIGHT_PRIORITIES
        elif follow == FOLLOW_LEFT:
            self.pika.priorities = FOLLOW_LEFT_PRIORITIES

    def solve(self):
        while not self.is_pikachu_back_at_the_start():
            priority_list = self.pika.priorities[self.pika.facing]
            self.pika.previous = (self.pika.x, self.pika.y)

            for priority in priority_list:
                if priority == RIGHT:
                    if self.pikachu_can_go_right():
                        self.pika.facing = RIGHT
                        self.pika.x += 1
                        break
                elif priority == DOWN:
                    if self.pikachu_can_go_down():
                        self.pika.facing = DOWN
                        self.pika.y += 1
                        break
                elif priority == LEFT:
                    if self.pikachu_can_go_left():
                        self.pika.facing = LEFT
                        self.pika.x -= 1
                        break
                elif priority == UP:
                    if self.pikachu_can_go_up():
                        self.pika.facing = UP
                        self.pika.y -= 1
                        break

            if self.pika.is_trapped():
                break
            self.rows[self.pika.y][self.pika.x] += 1

    def is_pikachu_back_at_the_start(self):
        return all([(self.pika.x, self.pika.y) == self.pika.start, self.rows[self.pika.y][self.pika.x] != 0])

    def pikachu_can_go_down(self):
        return self.pika.y < self.height - 1 and self.rows[self.pika.y + 1][self.pika.x] != WALL

    def pikachu_can_go_left(self):
        return self.pika.x > 0 and self.rows[self.pika.y][self.pika.x - 1] != WALL

    def pikachu_can_go_right(self):
        return self.pika.x < self.width - 1 and self.rows[self.pika.y][self.pika.x + 1] != WALL

    def pikachu_can_go_up(self):
        return self.pika.y > 0 and self.rows[self.pika.y - 1][self.pika.x] != WALL

    def print_solution(self):
        for y in range(self.height):
            for x in range(self.width):
                print(self.rows[y][x], end="")
            print()


if __name__ == "__main__":
    game = Game()
    game.read_input()
    game.solve()
    game.print_solution()
