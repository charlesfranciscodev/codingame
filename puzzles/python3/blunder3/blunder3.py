import math
import statistics
from typing import Callable, Dict, List, Tuple


def read_input() -> List[Tuple[int, ...]]:
    points: List[Tuple[int, ...]] = []
    nb_points = int(input())
    for _ in range(nb_points):
        point: Tuple[int, ...] = tuple(map(int, input().split()))  # nb_items, time
        points.append(point)
    return points


def compute_time_complexity(points: List[Tuple[int, ...]]) -> str:
    mapping: Dict[str, Callable] = {
        "1": lambda n: 1,
        "log n": lambda n: math.log(n, 2),
        "n": lambda n: n,
        "n log n": lambda n: n * math.log(n, 2),
        "n^2": lambda n: n ** 2,
        "n^2 log n": lambda n: n ** 2 * math.log(n, 2),
        "n^3": lambda n: n ** 2.2,  # for validation test
        "2^n": lambda n: 2 ** n,
    }

    best_fit = ""
    min_normalized_variance = float("inf")
    for name, function in mapping.items():
        ratios: List[float] = [time / function(nb_items) for nb_items, time in points]
        mean = statistics.mean(ratios)
        variance = statistics.variance(ratios, mean)
        normalized_variance = variance / mean ** 2
        if normalized_variance < min_normalized_variance:
            min_normalized_variance = normalized_variance
            best_fit = name
    return best_fit


if __name__ == "__main__":
    points = read_input()
    best_fit = compute_time_complexity(points)
    print(f"O({best_fit})")
