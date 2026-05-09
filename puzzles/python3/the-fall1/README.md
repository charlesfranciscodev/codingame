# The Fall - Episode 1

## Description

In this puzzle, the objective is to create a program that predicts the path of a character named Indy as he navigates a tunnel composed of various types of rooms. The tunnel is represented as a grid, and each room type has specific entrance and exit points. Indy starts at the top of the grid and moves downwards, and the program must determine his next position based on the current room type and entrance point. The goal is to continuously provide Indy's next position until he safely reaches the exit at the bottom of the tunnel. The challenge involves understanding and simulating Indy's movements through the tunnel's rooms using the given room types and entrance points.

## Code Example

```python
# Read the width and height of the grid
w, h = map(int, input().split())

# Read the grid and store room types
grid = []
for _ in range(h):
    row = list(map(int, input().split()))
    grid.append(row)

# Ignore the last line
input()

# Define a function to calculate Indy's next position
def next_position(x, y, pos, room_type):
    if room_type == 0:
        return x, y  # Indy cannot move in type 0 room
    
    if room_type == 1:
        return x, y + 1
    
    if room_type == 2 or room_type == 6:
        if pos == "LEFT":
            return x + 1, y
        elif pos == "RIGHT":
            return x - 1, y        
    
    if room_type == 3:
        if pos == "TOP":
            return x, y + 1
    
    if room_type == 4:
        if pos == "TOP":
            return x - 1, y
        elif pos == "RIGHT":
            return x, y + 1
    
    if room_type == 5:
        if pos == "TOP":
            return x + 1, y
        elif pos == "LEFT":
            return x, y + 1
    
    if room_type == 7:
        if pos == "TOP" or pos == "RIGHT":
            return x, y + 1
    
    if room_type == 8:
        if pos == "LEFT" or pos == "RIGHT":
            return x, y + 1
    
    if room_type == 9:
        return x, y + 1
    
    if room_type == 10:
        return x - 1, y
    
    if room_type == 11:
        return x + 1, y
    
    if room_type == 12:
        return x, y + 1
    
    if room_type == 13:
        return x, y + 1

# Infinite loop to read Indy's position and provide the next position
while True:
    xi, yi, pos = input().split()
    xi, yi = int(xi), int(yi)
    
    room_type = grid[yi][xi]
    x, y = next_position(xi, yi, pos, room_type)
    
    print(x, y)

```
