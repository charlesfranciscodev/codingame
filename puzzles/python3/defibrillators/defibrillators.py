import math

from typing import List


def to_radians(angle_in_degrees: str) -> float:
    return float(angle_in_degrees.replace(",", ".", 1)) * math.pi / 180


if __name__ == "__main__":
    min_distance = math.inf
    closest_defib_name = ""
    longitude = to_radians(input())
    latitude = to_radians(input())
    nb_defib = int(input())

    for _ in range(nb_defib):
        defib: List[str] = input().split(";")
        defib_longitude = to_radians(defib[4])
        defib_latitude = to_radians(defib[5])
        x = (defib_longitude - longitude) * math.cos((latitude + defib_latitude) / 2)
        y = defib_latitude - latitude
        EARTH_RADIUS: int = 6371
        distance = math.hypot(x, y) * EARTH_RADIUS
        if distance < min_distance:
            min_distance = distance
            closest_defib_name = defib[1]

    print(closest_defib_name)
