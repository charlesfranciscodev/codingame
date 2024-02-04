# Defibrillators

"Defibrillators" is a beginner-level coding challenge available on the CodinGame platform. In this challenge, the player is given the location of a person and the location of several defibrillators in a city, and is asked to determine the closest defibrillator to the person.

The input contains the location of the person as longitude and latitude, as well as the longitude and latitude of each defibrillator and its name. The player is asked to calculate the distance between the person and each defibrillator using the Haversine formula, which takes into account the curvature of the Earth's surface.

The challenge consists of writing a program that takes as input the location of the person and the locations of the defibrillators, and outputs the name of the closest defibrillator to the person.

The challenge is designed to help players learn and practice programming skills such as geographic coordinate manipulation, distance calculation, and data structures. It is a fun and engaging way to improve programming skills while solving a challenging and entertaining puzzle.

## Example Code

```python
import math

def convert_coordinates(coord):
    return math.radians(float(coord.replace(',', '.')))

def calculate_distance(user_longitude, user_latitude, defibrillator):
    defibrillator_longitude = convert_coordinates(defibrillator[4])
    defibrillator_latitude = convert_coordinates(defibrillator[5])
    x = (defibrillator_longitude - user_longitude) * math.cos((user_latitude + defibrillator_latitude) / 2)
    y = defibrillator_latitude - user_latitude
    return (x ** 2 + y ** 2) ** 0.5 * 6371

def find_nearest_defibrillator(user_longitude, user_latitude, defibrillators):
    user_longitude = convert_coordinates(user_longitude)
    user_latitude = convert_coordinates(user_latitude)
    min_distance = float('inf')
    nearest_defibrillator = ""
    for defibrillator in defibrillators:
        distance = calculate_distance(user_longitude, user_latitude, defibrillator)
        if distance < min_distance:
            min_distance = distance
            nearest_defibrillator = defibrillator[1]
    return nearest_defibrillator

# Read user's location
user_longitude = input()
user_latitude = input()

# Read the number of defibrillators
N = int(input())

# Read defibrillators' information
defibrillators = []
for _ in range(N):
    defibrillator = input().split(';')
    defibrillators.append(defibrillator)

# Find the nearest defibrillator
nearest_defibrillator = find_nearest_defibrillator(user_longitude, user_latitude, defibrillators)

# Output the result
print(nearest_defibrillator)

```

## Defibrillator Locator Logic

### Conversion of Coordinates
The code begins by defining a function to convert coordinates from a string format to radians. This conversion is essential for subsequent trigonometric calculations.

### Distance Calculation
Another function calculates the distance between the user's location and each defibrillator using the Haversine formula. This formula considers the curvature of the Earth and is suitable for small distances.

### Finding the Nearest Defibrillator
Iterating through the list of defibrillators, the code calculates the distance for each one and keeps track of the nearest defibrillator found so far. The minimum distance and corresponding defibrillator information are updated whenever a closer defibrillator is encountered.

### Input and Output
The script takes user input for their location, the number of defibrillators, and details about each defibrillator. After processing, it outputs the name of the nearest defibrillator based on the calculated distances.

This program essentially translates geographical coordinates into radians, computes distances with the Haversine formula, and identifies the closest defibrillator. It provides a practical solution for locating essential medical equipment in emergency situations.
