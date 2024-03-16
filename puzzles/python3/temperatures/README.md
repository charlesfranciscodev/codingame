# Temperatures

"Temperatures" is a beginner-level coding challenge available on the CodinGame platform. In this challenge, the player is given a list of integers representing temperature readings in Celsius degrees for a city during a certain period of time.

The objective is to write a program that finds and outputs the closest temperature to zero. If there are two temperatures that are equally close to zero, the program should output the positive one.

The challenge consists of writing a program that takes as input the list of temperature readings and outputs the temperature closest to zero. If the list is empty, the program should output 0.

The challenge is designed to help players learn and practice programming skills such as array manipulation, looping, and conditional statements. It is a fun and engaging way to improve programming skills while solving a challenging and entertaining puzzle.

## Code Example

```python
import sys

# Read the number of temperatures to analyze
n = int(input())

# Read the temperatures as a string and split it into a list of integers
temperatures = list(map(int, input().split()))

# Initialize variables to store the closest temperature
closest_temp = sys.maxsize
abs_closest_temp = sys.maxsize

# Iterate over each temperature
for temp in temperatures:
    # Calculate the absolute difference between the temperature and zero
    abs_diff = abs(temp)
    
    # Check if the current temperature is closer to zero
    if abs_diff < abs_closest_temp or (abs_diff == abs_closest_temp and temp > closest_temp):
        closest_temp = temp
        abs_closest_temp = abs_diff

# Print the closest temperature
print(closest_temp if n > 0 else 0)

```

## Edge Cases

These include scenarios such as an empty input list, all negative temperatures, all positive temperatures, temperatures equidistant from zero with opposite signs, a single temperature in the list, and a large range of temperatures. Testing with an empty list ensures the program outputs 0 as expected, while all negative and positive temperatures verify whether the program identifies the closest positive temperature to zero correctly. Similarly, testing temperatures equidistant from zero with opposite signs checks the program's output in such cases. Additionally, testing with a single temperature ensures the program handles single-item lists accurately, and providing a large range of temperatures evaluates the program's efficiency and performance.
