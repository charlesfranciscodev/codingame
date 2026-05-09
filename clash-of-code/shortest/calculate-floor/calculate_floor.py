def calculate_floor(log):
    current_floor = 0

    for char in log:
        if char == "(":
            current_floor += 1
        elif char == ")":
            current_floor -= 1

    return current_floor
