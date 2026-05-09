import math
from typing import List


def convert_coordinates(coord: str) -> float:
    return math.radians(float(coord.replace(",", ".")))


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


# Read user's location
user_longitude = input()
user_latitude = input()

# Read the number of defibrillators
N = int(input())

# Read defibrillators' information
defibrillators = []
for _ in range(N):
    defibrillator = input().split(";")
    defibrillators.append(defibrillator)

# Find the nearest defibrillator
nearest_defibrillator = find_nearest_defibrillator(user_longitude, user_latitude, defibrillators)

# Output the result
print(nearest_defibrillator)
