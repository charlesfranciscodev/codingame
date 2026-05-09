from typing import Dict, List, Tuple


if __name__ == "__main__":
    nb_places, nb_rides, nb_groups = map(int, input().split())
    groups: List[int] = []
    memo: Dict[int, Tuple[int, int]] = {}  # group index => (earnings, next_group_index)
    for _ in range(nb_groups):
        groups.append(int(input()))

    # calculate earnings starting from each group/subproblem
    for start_index in range(nb_groups):
        total_group_size = 0
        index = start_index
        while total_group_size + groups[index] <= nb_places:
            total_group_size += groups[index]
            index += 1
            if index == nb_groups:
                index = 0
            if index == start_index:
                break
        memo[start_index] = (total_group_size, index)

    # calculate total earnings during the day
    total_earnings = 0
    index = 0
    for _ in range(nb_rides):
        earnings, next_group_index = memo[index]
        total_earnings += earnings
        index = next_group_index

    print(total_earnings)
