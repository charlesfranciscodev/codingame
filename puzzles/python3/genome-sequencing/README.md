# Genome Sequencing

The puzzle is asking for the length of the shortest sequence that contains all the given sub-sequences. The approach is to iterate through permutations of the input sub-sequences and, for each permutation, find the shortest common supersequence. The supersequence is constructed by extending the initial sequence with additional characters from the remaining sub-sequences.

## Solution

- The function takes a list of permutations as input.
- For each permutation, it initializes a string with the first sub-sequence.
- It then iterates through the remaining sub-sequences and extends the current supersequence to include characters from each sub-sequence.
- The loop checks for the commonality of characters and appends the necessary characters to the supersequence.
- The length of the resulting supersequence is compared with the current minimum length.
- Finally, the function returns the minimum length of the supersequence.

```python
from itertools import permutations

def find_shortest_supersequence_length(seqs: list[str]) -> int:
    min_len = float('inf')

    for perm in permutations(seqs):
        cur_superseq = perm[0]

        for j in range(1, len(perm)):
            i = 0

            while i < len(cur_superseq):
                if cur_superseq.find(perm[j]) != -1:
                    break
                elif cur_superseq[i:] == perm[j][:len(cur_superseq) - i]:
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
```
