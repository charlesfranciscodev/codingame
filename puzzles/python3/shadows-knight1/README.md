# Shadows of the Knight - Episode 1

This is a solution to the "Shadows of the Knight - Episode 1" puzzle on CodinGame.

## Solution Overview

To solve this puzzle using a 2D Binary Search algorithm, we can narrow down the search space by updating our current position based on the direction indicated by the heat-signature device.

This algorithm works by narrowing down the search boundaries for the next jump based on the indicated direction. It then calculates the next jump position using binary search on the narrowed boundaries. The algorithm repeats this process for each turn, updating the search boundaries and calculating the next jump position accordingly.

## Example Code

```python
# Read initialization data
W, H = map(int, input().split())
N = int(input())
X0, Y0 = map(int, input().split())

# Define directions as vectors (dx, dy)
directions = {
    'U': (0, -1),
    'UR': (1, -1),
    'R': (1, 0),
    'DR': (1, 1),
    'D': (0, 1),
    'DL': (-1, 1),
    'L': (-1, 0),
    'UL': (-1, -1)
}

# Initialize search boundaries
left, right = 0, W - 1
top, bottom = 0, H - 1

# Game loop
for _ in range(N):
    direction = input().strip()

    # Update search boundaries based on direction
    dx, dy = directions[direction]
    if dx < 0:
        right = X0 - 1
    elif dx > 0:
        left = X0 + 1
    if dy < 0:
        bottom = Y0 - 1
    elif dy > 0:
        top = Y0 + 1

    # Calculate next jump position using binary search
    next_x = (left + right) // 2
    next_y = (top + bottom) // 2

    # Output next jump position
    print(next_x, next_y)
    X0, Y0 = next_x, next_y

```

## Conclusion

The "Shadows of the Knight - Episode 1" puzzle is a simple example of a search problem that can be solved using a binary search algorithm. The solution presented here demonstrates the basic concepts involved in solving such problems and can be used as a starting point for more complex search problems.
