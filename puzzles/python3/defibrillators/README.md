# Defibrillators

"Defibrillators" is a beginner-level coding challenge available on the CodinGame platform. In this challenge, the player is given the location of a person and the location of several defibrillators in a city, and is asked to determine the closest defibrillator to the person.

## Example Code

```python
import math
from typing import List, Tuple

def convert_coordinates(coord: str) -> float:
    return math.radians(float(coord.replace(',', '.')))

def calculate_distance(user_longitude: float, user_latitude: float, defibrillator: List[str]) -> float:
    defibrillator_longitude = convert_coordinates(defibrillator[4])
    defibrillator_latitude = convert_coordinates(defibrillator[5])
    x = (defibrillator_longitude - user_longitude) * math.cos((user_latitude + defibrillator_latitude) / 2)
    y = defibrillator_latitude - user_latitude
    return math.hypot(x, y) * 6371

def find_nearest_defibrillator(user_longitude: float, user_latitude: float, defibrillators: List[List[str]]) -> str:
    user_longitude = convert_coordinates(user_longitude)
    user_latitude = convert_coordinates(user_latitude)
    min_distance = math.inf
    nearest_defibrillator = ""
    for defibrillator in defibrillators:
        distance = calculate_distance(user_longitude, user_latitude, defibrillator)
        if distance < min_distance:
            min_distance = distance
            nearest_defibrillator = defibrillator[1]
    return nearest_defibrillator

user_longitude = input()
user_latitude = input()

N = int(input())

defibrillators = []
for _ in range(N):
    defibrillator = input().split(';')
    defibrillators.append(defibrillator)

nearest_defibrillator = find_nearest_defibrillator(user_longitude, user_latitude, defibrillators)

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
