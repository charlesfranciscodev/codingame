from typing import List


if __name__ == "__main__":
    nb_buildings = int(input())
    y_coordinates: List[int] = []
    min_x = 2 ** 30
    max_x = -2 ** 30

    for _ in range(nb_buildings):
        x, y = map(int, input().split())
        y_coordinates.append(y)
        if x < min_x:
            min_x = x
        if x > max_x:
            max_x = x

    # length of horizontal cable
    cable_length = max_x - min_x

    # calculate y median to minimize the length of vertical cable(s)
    y_coordinates.sort()
    y_median: int = y_coordinates[nb_buildings // 2]

    # length of vertical cable(s)
    for y in y_coordinates:
        cable_length += abs(y_median - y)

    print(cable_length)
