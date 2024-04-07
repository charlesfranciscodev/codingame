def count_valid_codes(input_str):
    digits = [int(d) for d in input_str if int(d) > 4]
    unique_digits = set(digits)
    return len(unique_digits)


def calculate_combinations(valid_count):
    if valid_count < 3:
        return "No codes"
    else:
        return valid_count * (valid_count - 1) * (valid_count - 2)


if __name__ == '__main__':
    input_str = input()
    valid_count = count_valid_codes(input_str)
    result = calculate_combinations(valid_count)
    print(result)
