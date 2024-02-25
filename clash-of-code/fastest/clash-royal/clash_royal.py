def calculate_damage(level):
    return 200 + (level - 1) * 20


def clash_royal_match(health, level):
    damage = calculate_damage(level)
    health -= damage

    if health <= 0:
        return "hehehehaw", health
    else:
        return "rawr", health


if __name__ == '__main__':
    # Get input
    health = int(input())
    level = int(input())

    # Call the function and print the output
    result, remaining_health = clash_royal_match(health, level)
    print(result, remaining_health)
