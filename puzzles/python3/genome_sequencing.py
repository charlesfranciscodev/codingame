import itertools
from typing import List, Tuple


def read_game_input():
    subsequences: List[str] = []
    n = int(input())
    for _ in range(n):
        subsequences.append(input())
    return subsequences


def compute_min_subseq_length(subsequences: List[str]) -> int:
    permutations: List[Tuple[str, ...]] = list(itertools.permutations(subsequences))
    min_length = 60
    for permutation in permutations:
        sequence = permutation[0]
        for i in range(1, len(permutation)):
            j = 0
            while j < len(sequence):
                subsequence = permutation[i]
                # check if the subsequence is contained within the sequence
                if sequence.find(subsequence) != -1:
                    break
                # check if there is a partial match
                end_index = len(sequence) - j
                if sequence[j:] == subsequence[:end_index]:
                    sequence += subsequence[end_index:]
                j += 1
            # check if there is no match
            if j == len(sequence):
                sequence += subsequence
        min_length = min(min_length, len(sequence))
    return min_length


if __name__ == "__main__":
    subsequences: List[str] = read_game_input()
    min_length = compute_min_subseq_length(subsequences)
    print(min_length)
