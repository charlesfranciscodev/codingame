if __name__ == "__main__":
    surface_n = int(input())
    for _ in range(surface_n):
        land_x, land_y = map(int, input().split())

    # game loop
    while True:
        # v_speed: the vertical speed (in m/s), can be negative.
        # power: the thrust power (0 to 4).
        _, _, _, v_speed, _, _, power = map(int, input().split())

        if v_speed <= -40:
            power = min(4, power + 1)
        else:
            power = max(0, power - 1)

        # 2 integers: rotate power.
        print(f"0 {power}")
