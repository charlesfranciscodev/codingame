from typing import List


def closest_to_zero(temperatures: List[int]):
    min_temperature = 5526
    for temperature in temperatures:
        if any([
            abs(temperature) < abs(min_temperature),
            abs(temperature) == abs(min_temperature) and temperature > min_temperature
        ]):
            min_temperature = temperature

    return 0 if len(temperatures) == 0 else min_temperature


if __name__ == "__main__":
    # the number of temperatures to analyse
    n = int(input())
    temperatures = list(map(int, input().split()))
    print(closest_to_zero(temperatures))
