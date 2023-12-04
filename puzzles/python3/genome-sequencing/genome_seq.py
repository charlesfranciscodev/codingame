from itertools import permutations


def find_shortest_supersequence_length(seqs: list[str]) -> int:
    min_len = float("inf")

    for perm in permutations(seqs):
        cur_superseq = perm[0]

        for j in range(1, len(perm)):
            i = 0

            while i < len(cur_superseq):
                if cur_superseq.find(perm[j]) != -1:
                    break
                elif cur_superseq[i:] == perm[j][: len(cur_superseq) - i]:
                    cur_superseq += perm[j][len(cur_superseq) - i:]
                    break
                i += 1

            if i == len(cur_superseq):
                cur_superseq += perm[j]

        min_len = min(len(cur_superseq), min_len)

    return min_len


# Reading input from command line
N = int(input())
seqs = [input() for _ in range(N)]

# Outputting the result
print(find_shortest_supersequence_length(seqs))
