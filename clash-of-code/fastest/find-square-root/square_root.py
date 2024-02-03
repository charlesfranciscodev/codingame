import math


def find_square_root(N, numbers):
    if N == 0:
        return 0

    # Find the lowest and highest numbers in the list
    lowest = min(numbers)
    highest = max(numbers)

    # Calculate the product of the lowest and highest numbers
    product = lowest * highest

    # Calculate the square root of the product and round down
    result = math.floor(math.sqrt(product))

    return result


if __name__ == "__main__":
    # Input
    N = int(input())
    numbers = [int(input()) for _ in range(N)]

    # Output
    output = find_square_root(N, numbers)
    print(output)
