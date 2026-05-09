def calculate_actual_weight(body_weight, repetitions, exercise_type, added_weight):
    if exercise_type == "bp":
        actual_weight = (added_weight + 20) * repetitions
    elif exercise_type == "lp":
        actual_weight = (added_weight + 47) * repetitions
    elif exercise_type == "p":
        actual_weight = added_weight + body_weight
    else:
        actual_weight = 0

    return actual_weight


if __name__ == "__main__":
    # Get input from the user
    body_weight = int(input())
    repetitions = int(input())
    exercise_type = input()
    added_weight = int(input())

    # Calculate the actual weight
    actual_weight = calculate_actual_weight(body_weight, repetitions, exercise_type, added_weight)

    # Output the result
    print(actual_weight)
