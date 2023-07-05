import unittest

from the_gift import calculate_contributions


class TestCalculateContributions(unittest.TestCase):
    def test_impossible_case(self):
        N = 3
        C = 100
        budgets = [20, 20, 40]
        expected_output = None
        self.assertEqual(calculate_contributions(N, C, budgets), expected_output)

    def test_possible_case_2(self):
        N = 3
        C = 100
        budgets = [40, 40, 40]
        expected_output = [33, 33, 34]
        self.assertEqual(calculate_contributions(N, C, budgets), expected_output)

    def test_possible_case_3(self):
        N = 3
        C = 100
        budgets = [100, 1, 60]
        expected_output = [1, 49, 50]
        self.assertEqual(calculate_contributions(N, C, budgets), expected_output)


if __name__ == "__main__":
    unittest.main()
