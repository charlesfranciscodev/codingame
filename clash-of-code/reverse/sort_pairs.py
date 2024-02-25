def sort_pairs(numbers):
    for i in range(0, len(numbers), 2):
        numbers[i : i + 2] = sorted(numbers[i : i + 2])
    return numbers


# Test cases
tests = [
    ([1, 2, 6, 5, 4], [1, 2, 5, 6, 4]),
    ([9, 8, 6, 7, 5, 4, 3], [8, 9, 6, 7, 4, 5, 3]),
    ([1000], [1000]),
    ([54, 21, 6, 33, 14, 70, 20, 88, 99, 14], [21, 54, 6, 33, 14, 70, 20, 88, 14, 99]),
]

# Perform the tests
for i, (input_list, expected_output) in enumerate(tests):
    result = sort_pairs(input_list)
    assert result == expected_output, f"Test {i+1} failed: Expected {expected_output}, got {result}"
    print(f"Test {i+1}: Passed")
