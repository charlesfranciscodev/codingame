def find_odd_squares(numbers):
    odd_numbers = [n for n in numbers if n % 2 != 0]
    square_set = set(n**2 for n in odd_numbers)
    sorted_squares = sorted(square_set, reverse=True)
    return sorted_squares


def main():
    _ = int(input().strip())
    integers = list(map(int, input().strip().split()))

    result = find_odd_squares(integers)
    print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()
