from typing import List


if __name__ == "__main__":
    EMPTY = '.'
    NODE = '0'
    grid: List[str] = []

    width = int(input())  # the number of cells on the X axis
    height = int(input())  # the number of cells on the Y axis
    for _ in range(height):
        grid.append(input())

    for y in range(height):
        for x in range(width):
            if grid[y][x] == NODE:
                # node
                output = f"{x} {y} "

                # right neighbor
                neighbor = EMPTY
                for neighbor_x in range(x + 1, width):
                    neighbor = grid[y][neighbor_x]
                    if neighbor == NODE:
                        output += f"{neighbor_x} {y} "
                        break

                if neighbor == EMPTY:
                    output += "-1 -1 "

                # bottom neighbor
                neighbor = EMPTY
                for neighbor_y in range(y + 1, height):
                    neighbor = grid[neighbor_y][x]
                    if neighbor == NODE:
                        output += f"{x} {neighbor_y} "
                        break

                if neighbor == EMPTY:
                    output += "-1 -1 "

                print(output)
