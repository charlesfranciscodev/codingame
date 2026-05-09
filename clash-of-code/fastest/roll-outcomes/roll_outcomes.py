def read_input():
    nbRoll = int(input())
    rolls = []
    expected_values = []
    for _ in range(nbRoll):
        roll, expected = map(int, input().split())
        rolls.append(roll)
        expected_values.append(expected)
    return nbRoll, rolls, expected_values


def determine_outcome(roll, expected):
    if roll == 20:
        return "Critical Success"
    elif roll == 1:
        return "Critical Failure"
    elif roll >= expected:
        return "Success"
    else:
        return "Failure"


def roll_outcomes(nbRoll, rolls, expected_values):
    outcomes = []
    for i in range(nbRoll):
        outcome = determine_outcome(rolls[i], expected_values[i])
        outcomes.append(outcome)
    return outcomes


if __name__ == "__main__":
    # Read the input
    nbRoll, rolls, expected_values = read_input()

    # Get the outcomes of the rolls
    outcomes = roll_outcomes(nbRoll, rolls, expected_values)

    # Print the outcomes
    for outcome in outcomes:
        print(outcome)
