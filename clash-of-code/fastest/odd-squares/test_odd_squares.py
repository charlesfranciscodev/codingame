import unittest

from odd_squares import find_odd_squares


class TestFindOddSquares(unittest.TestCase):
    def test_single_odd_number(self):
        numbers = [3]
        expected_output = [9]
        self.assertEqual(find_odd_squares(numbers), expected_output)

    def test_multiple_odd_numbers(self):
        numbers = [1, 2, 3, 4, 5]
        expected_output = [25, 9, 1]
        self.assertEqual(find_odd_squares(numbers), expected_output)

    def test_duplicate_odd_numbers(self):
        numbers = [1, 1, 3, 3, 5, 5]
        expected_output = [25, 9, 1]
        self.assertEqual(find_odd_squares(numbers), expected_output)

    def test_mixed_numbers(self):
        numbers = [2, 3, 4, 5, 6, 7]
        expected_output = [49, 25, 9]
        self.assertEqual(find_odd_squares(numbers), expected_output)

    def test_negative_numbers(self):
        numbers = [-3, -1, 1, 3, 5]
        expected_output = [25, 9, 1]
        self.assertEqual(find_odd_squares(numbers), expected_output)

    def test_empty_list(self):
        numbers = []
        expected_output = []
        self.assertEqual(find_odd_squares(numbers), expected_output)


if __name__ == "__main__":
    unittest.main()
