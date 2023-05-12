from typing import List


def solve(mountain_heights: List[int]) -> int:
    index_to_fire = 0
    max_mountain_height = -1
    for index, mountain_height in enumerate(mountain_heights):
        if mountain_height > max_mountain_height:
            max_mountain_height = mountain_height
            index_to_fire = index
    return index_to_fire


if __name__ == "__main__":
    while True:
        mountain_heights = [int(input()) for _ in range(8)]
        print(solve(mountain_heights))
