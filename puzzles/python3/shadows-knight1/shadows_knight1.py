if __name__ == "__main__":
    width, height = map(int,  input().split())
    nb_turns = int(input())
    x, y = map(int, input().split())

    min_x = 0
    max_x = width - 1
    min_y = 0
    max_y = height - 1

    # game loop
    while True:
        bomb_dir = input()

        if bomb_dir == "U":
            max_y = y - 1
            min_x = max_x = x
        elif bomb_dir == "UR":
            min_x = x + 1
            max_y = y - 1
        elif bomb_dir == "R":
            min_x = x + 1
            min_y = max_y = y
        elif bomb_dir == "DR":
            min_x = x + 1
            min_y = y + 1
        elif bomb_dir == "D":
            min_y = y + 1
            min_x = max_x = x
        elif bomb_dir == "DL":
            max_x = x - 1
            min_y = y + 1
        elif bomb_dir == "L":
            max_x = x - 1
            min_y = max_y = y
        elif bomb_dir == "UL":
            max_x = x - 1
            max_y = y - 1

        x = int((min_x + max_x) / 2)
        y = int((min_y + max_y) / 2)
        # the location of the next window Batman should jump to.
        print(f"{x} {y}")
