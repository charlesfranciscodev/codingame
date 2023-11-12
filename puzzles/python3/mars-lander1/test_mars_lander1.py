from io import StringIO
from contextlib import redirect_stdout

from mars_lander1 import solve


def test_solve_with_negative_v_speed():
    v_speed = -45
    power = 2
    expected_result = (0, min(4, power + 1))

    assert solve(v_speed, power) == expected_result


def test_solve_with_positive_v_speed():
    v_speed = -30
    power = 3
    expected_result = (0, max(0, power - 1))

    assert solve(v_speed, power) == expected_result


def test_loop():
    input_data = "2\n10 20\n30 40\n-5 6 7 -20 -15 0 2\n"
    expected_output = "0 3\n"

    with StringIO(input_data) as _, StringIO() as stdout:
        with redirect_stdout(stdout):
            exec(open("your_code.py").read())

        assert stdout.getvalue() == expected_output


if __name__ == "__main__":
    test_solve_with_negative_v_speed()
    test_solve_with_positive_v_speed()
