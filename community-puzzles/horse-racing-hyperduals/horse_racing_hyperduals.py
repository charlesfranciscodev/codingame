import math
from typing import List, Tuple


def find_closest_pair(vectors: List) -> int:
    # Sort points by x-coordinate
    vectors.sort(key=lambda x: x[0])

    # Find the closest pair recursively
    return find_closest_pair_recursive(vectors)


def find_closest_pair_recursive(vectors: List) -> int:
    n = len(vectors)

    # Base case: if there are only two or three points, calculate the distance directly
    if n <= 3:
        return find_min_dist_base_case(vectors)

    # Divide the set of points into two equal-sized subsets
    mid = n // 2
    left_subset = vectors[:mid]
    right_subset = vectors[mid:]

    # Recursively find the closest pair in each subset
    min_left = find_closest_pair_recursive(left_subset)
    min_right = find_closest_pair_recursive(right_subset)

    # Find the minimum distance between the closest pairs of the two subsets
    min_distance = min(min_left, min_right)

    # Merge the two subsets by the median x-coordinate
    median_x = (vectors[mid - 1][0] + vectors[mid][0]) / 2
    mid_region = []
    for vector in vectors:
        if abs(vector[0] - median_x) < min_distance:
            mid_region.append(vector)

    # Sort the strip by y-coordinate
    mid_region.sort(key=lambda x: x[1])

    # Find the closest pair within the strip
    min_mid_region_dist = find_mid_region_dist(mid_region, min_distance)

    # Return the minimum distance among all pairs
    return min(min_distance, min_mid_region_dist)


def find_min_dist_base_case(vectors: List) -> int:
    min_distance = math.inf
    for i in range(len(vectors)):
        for j in range(i + 1, len(vectors)):
            min_distance = min(min_distance, distance(vectors[i], vectors[j]))
    return min_distance


def find_mid_region_dist(mid_region: List, min_distance: int) -> int:
    for i in range(len(mid_region)):
        j = i + 1
        while j < len(mid_region) and (mid_region[j][1] - mid_region[i][1]) < min_distance:
            min_distance = min(min_distance, distance(mid_region[i], mid_region[j]))
            j += 1
    return min_distance


def distance(vector1: Tuple, vector2: Tuple) -> int:
    # Manhattan Distance
    return abs(vector2[0] - vector1[0]) + abs(vector2[1] - vector1[1])


if __name__ == "__main__":
    n = int(input())
    vectors = []
    for i in range(n):
        vector = tuple(map(int, input().split()))
        vectors.append(vector)

    min_distance = find_closest_pair(vectors)

    print(min_distance)
