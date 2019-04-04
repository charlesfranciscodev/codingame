# Approximation using a Greedy Algorithm
import math


def distance(point1, point2):
    dx = point2[0] - point1[0]
    dy = point2[1] - point1[1]
    return math.hypot(dx, dy)


if __name__ == "__main__":
    unvisited = set()
    total_dist = 0
    current_index = 0
    points = []

    n = int(input())
    for i in range(n):
        point = tuple(map(int, input().split()))  # x, y
        points.append(point)
        unvisited.add(i)

    while (len(unvisited) != 0):
        min_index = 0
        min_dist = math.inf
        current_point = points[current_index]
        for i in unvisited:
            if (i != 0):
                dist = distance(current_point, points[i])
                if (dist < min_dist):
                    min_dist = dist
                    min_index = i
        if (min_index == 0):
            min_dist = distance(current_point, points[0])
        total_dist += min_dist
        unvisited.remove(min_index)
        current_index = min_index

    print(round(total_dist))
