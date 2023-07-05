from compute_sums import compute_sums


def main():
    test_cases = [
        (4, (10, 30, 100)),
        (10, (55, 385, 3025)),
        (1, (1, 1, 1)),
        # Add more test cases here if needed
    ]

    for n, expected_result in test_cases:
        result = compute_sums(n)
        if result == expected_result:
            print(f"Test case for n={n} passed")
        else:
            print(f"Test case for n={n} failed. Expected {expected_result}, but got {result}")


if __name__ == "__main__":
    main()
