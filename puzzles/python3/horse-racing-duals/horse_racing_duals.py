from typing import List


if __name__ == "__main__":
    strengths: List[int] = []
    min_diff = 10000000
    n = int(input())
    for _ in range(n):
        strengths.append(int(input()))

    strengths.sort()

    for i in range(n - 1):
        diff = strengths[i + 1] - strengths[i]
        if diff < min_diff:
            min_diff = diff

    print(min_diff)
