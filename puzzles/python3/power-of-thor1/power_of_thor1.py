from typing import Tuple


def solve(light_x: int, light_y: int, thor_x: int, thor_y: int) -> Tuple[str, int, int]:
    direction = ""

    if thor_y > light_y:
        direction += "N"
        thor_y -= 1
    elif thor_y < light_y:
        direction += "S"
        thor_y += 1

    if thor_x > light_x:
        direction += "W"
        thor_x -= 1
    elif thor_x < light_x:
        direction += "E"
        thor_x += 1

    return direction, thor_x, thor_y


if __name__ == "__main__":
    light_x, light_y, thor_x, thor_y = map(int, input().split())

    # game loop
    while True:
        direction, thor_x, thor_y = solve(light_x, light_y, thor_x, thor_y)
        print(direction)
