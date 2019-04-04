import math


def distance(vector1, vector2):
    return abs(vector2[0] - vector1[0]) + abs(vector2[1] - vector1[1])


if __name__ == "__main__":
    n = int(input())
    vectors = []
    for i in range(n):
        vector = tuple(map(int, input().split()))
        vectors.append(vector)

    min_d = math.inf
    for i in range(n):
        for j in range(i + 1, n):
            d = distance(vectors[i], vectors[j])
            min_d = min(min_d, d)

    print(min_d)
