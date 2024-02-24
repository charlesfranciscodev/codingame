import unittest

from calc_weight import calculate_actual_weight


class TestCalculateActualWeight(unittest.TestCase):
    def test_bench_press(self):
        actual_weight = calculate_actual_weight(70, 5, "bp", 10)
        self.assertEqual(actual_weight, (10 + 20) * 5)

    def test_leg_press(self):
        actual_weight = calculate_actual_weight(70, 8, "lp", 15)
        self.assertEqual(actual_weight, (15 + 47) * 8)

    def test_pull_up(self):
        actual_weight = calculate_actual_weight(70, 6, "p", 0)
        self.assertEqual(actual_weight, 70)

    def test_invalid_exercise_type(self):
        actual_weight = calculate_actual_weight(70, 6, "xyz", 10)
        self.assertEqual(actual_weight, 0)


if __name__ == "__main__":
    unittest.main()
