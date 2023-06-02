from roll_outcomes import determine_outcome


def test_determine_outcome():
    # Test cases for roll = 20
    outcome = determine_outcome(20, 10)
    assert outcome == "Critical Success"

    outcome = determine_outcome(20, 20)
    assert outcome == "Critical Success"

    # Test cases for roll = 1
    outcome = determine_outcome(1, 10)
    assert outcome == "Critical Failure"

    outcome = determine_outcome(1, 1)
    assert outcome == "Critical Failure"

    # Test cases for roll >= expected
    outcome = determine_outcome(15, 10)
    assert outcome == "Success"

    outcome = determine_outcome(10, 10)
    assert outcome == "Success"

    # Test cases for roll < expected
    outcome = determine_outcome(8, 10)
    assert outcome == "Failure"

    outcome = determine_outcome(4, 10)
    assert outcome == "Failure"

    print("All tests passed.")


# Run the unit tests
test_determine_outcome()
