import math


def xp_for_level_up(level):
    return math.floor(level * math.sqrt(level) * 10)


if __name__ == "__main__":
    XP_GAIN = 300
    level = int(input())
    xp_needed = int(input())
    nb_puzzles = int(input())

    xp_gained = (nb_puzzles * XP_GAIN) + (xp_for_level_up(level) - xp_needed)
    while xp_gained >= xp_for_level_up(level):
        xp_gained -= xp_for_level_up(level)
        level += 1
    xp_needed = xp_for_level_up(level) - xp_gained

    print(level)
    print(xp_needed)
