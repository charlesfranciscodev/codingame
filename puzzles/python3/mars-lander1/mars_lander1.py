from typing import Tuple


def solve(v_speed: int, power: int) -> Tuple[int, int]:
    if v_speed <= -40:
        power = min(4, power + 1)
    else:
        power = max(0, power - 1)
    return 0, power


if __name__ == "__main__":
    # ignoring this input for level 1
    surface_n = int(input())
    for _ in range(surface_n):
        _ = input()

    # game loop
    while True:
        # v_speed: the vertical speed (in m/s), can be negative.
        # power: the thrust power (0 to 4).
        _, _, _, v_speed, _, _, power = map(int, input().split())
        rotate, power = solve(v_speed, power)
        print(f"{rotate} {power}")
