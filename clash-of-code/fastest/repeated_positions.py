import sys
from collections import Counter

routes = input()
counter = Counter()
position = (0, 0)  # (x, y)
counter[position] += 1

for route in routes:
    if route == '^':
        position = (position[0], position[1] - 1)
    elif route == '>':
        position = (position[0] + 1, position[1])
    elif route == 'v':
        position = (position[0], position[1] + 1)
    elif route == "<":
        position = (position[0] - 1, position[1])
    counter[position] += 1

print(counter.most_common(1)[0][1])
