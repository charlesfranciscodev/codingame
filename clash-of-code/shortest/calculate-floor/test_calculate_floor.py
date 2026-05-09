from calculate_floor import calculate_floor


def test_calculate_floor():
    assert calculate_floor("(()())") == 0
    assert calculate_floor("())())())") == -3
    assert calculate_floor("((())()") == 1
    assert calculate_floor("()()()()") == 0
    assert calculate_floor(")(") == 0
    assert calculate_floor("(") == 1
    assert calculate_floor(")") == -1
    assert calculate_floor("") == 0
    assert calculate_floor("()()(()()())(()()())()") == 0


if __name__ == "__main__":
    test_calculate_floor()
