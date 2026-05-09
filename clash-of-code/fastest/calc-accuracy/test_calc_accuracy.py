from calc_accuracy import calculate_accuracy


def test_calculate_accuracy():
    # key and submission are identical
    key = "hello"
    submission = "hello"
    assert calculate_accuracy(key, submission) == 1.0

    # key and submission have some matching characters
    key = "hello"
    submission = "helps"
    assert calculate_accuracy(key, submission) == 0.6

    # key and submission have no matching characters
    key = "hello"
    submission = "world"
    assert calculate_accuracy(key, submission) == 0.2

    # empty key and empty submission
    key = ""
    submission = ""
    assert calculate_accuracy(key, submission) == 1.0

    # long key and long submission with some matching characters
    key = "abcdefghijklmnopqrstuvwxyz"
    submission = "abcdefghijklmnopqrstuvwxyy"
    assert calculate_accuracy(key, submission) == 0.9615384615384616

    # long key and long submission with no matching characters
    key = "abcdefghijklmnopqrstuvwxyz"
    submission = "1234567890!@#$%^&*()"
    assert calculate_accuracy(key, submission) == 0.0


if __name__ == "__main__":
    test_calculate_accuracy()
