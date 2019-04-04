from collections import Counter

counter = Counter()
x = input()
for c in x:
    counter[c] += 1
    for i in range(0, counter[c]):
        print(c, end='')
