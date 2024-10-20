# Mars Lander - Episode 1

## Description

"Mars Lander - Episode 1" is a beginner-level coding challenge available on the CodinGame platform. In this challenge, the player takes on the role of a spaceship pilot trying to safely land a spacecraft on the surface of Mars.

The player is given the coordinates and the speed of the spacecraft, as well as the angle of its trajectory and the thrust power to be used to adjust its speed and direction. The objective is to write a program that computes the optimal thrust power and angle for the spacecraft to land safely on the surface of Mars without crashing or running out of fuel.

The challenge consists of writing a program that takes as input the current state of the spacecraft and outputs the thrust power and angle that should be used to adjust its trajectory and speed for a safe landing. The program needs to take into account the gravitational pull of Mars, the speed of the spacecraft, the remaining fuel, and the altitude of the spacecraft above the surface of Mars.

## Solution Overview

The algorithm starts by reading the surface data. Then, it enters an infinite loop, continually reading the current state of the spacecraft and calculating the new thrust power based on the vertical speed. The thrust power is adjusted by one unit if the vertical speed exceeds the maximum allowed, and the new power value is adjusted to be within the valid range. The thrust power is adjusted by one unit if the vertical speed is below the minimum allowed, and the new power value is adjusted to be within the valid range. Finally, the new thrust power and rotation angle are printed to the console.

## Code Example

```python
# Constants
MAX_VERTICAL_SPEED = 40
MAX_POWER = 4

def read_surface_data():
    surface_count = int(input())
    for _ in range(surface_count):
        _, _ = map(int, input().split())

def calculate_thrust_power(v_speed, power):
    if v_speed <= -MAX_VERTICAL_SPEED:
        power = min(power + 1, MAX_POWER)
    elif v_speed >= MAX_VERTICAL_SPEED:
        power = max(power - 1, 0)
    return power

def main():
    read_surface_data()

    while True:
        _, _, h_speed, v_speed, _, _, power = map(int, input().split())

        power = calculate_thrust_power(v_speed, power)
        rotate = 0

        print(rotate, power)

if __name__ == '__main__':
    main()

```
