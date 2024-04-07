from math import factorial
from typing import Tuple


def product_and_sum_of_consecutive_integers(n: int) -> Tuple[int, int]:
    product = factorial(n)
    total_sum = n * (n + 1) // 2
    return product, total_sum


if __name__ == "__main__":
    n = int(input())
    product, total_sum = product_and_sum_of_consecutive_integers(n)
    print(product)
    print(total_sum)
