import unittest
from count_working_codes import count_valid_codes, calculate_combinations


class TestCountValidCodes(unittest.TestCase):
    def test_no_valid_codes(self):
        self.assertEqual(count_valid_codes(""), 0)
        self.assertEqual(count_valid_codes("1234"), 0)

    def test_valid_codes(self):
        self.assertEqual(count_valid_codes("555555"), 1)
        self.assertEqual(count_valid_codes("5678"), 4)
        self.assertEqual(count_valid_codes("567891"), 5)


class TestCalculateCombinations(unittest.TestCase):
    def test_valid_count_less_than_3(self):
        for count in range(0, 3):
            self.assertEqual(calculate_combinations(count), "No codes")

    def test_valid_count_greater_than_or_equal_to_3(self):
        self.assertEqual(calculate_combinations(5), 60)
        self.assertEqual(calculate_combinations(4), 24)
        self.assertEqual(calculate_combinations(3), 6)


if __name__ == "__main__":
    unittest.main()
