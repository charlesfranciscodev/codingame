import unittest

from temperatures import closest_to_zero


class ClosestToZeroTestCase(unittest.TestCase):
    def test_empty_list(self):
        temperatures = []
        self.assertEqual(closest_to_zero(temperatures), 0)

    def test_positive_temperatures(self):
        temperatures = [10, 5, 3, 8]
        self.assertEqual(closest_to_zero(temperatures), 3)

    def test_negative_temperatures(self):
        temperatures = [-10, -5, -3, -8]
        self.assertEqual(closest_to_zero(temperatures), -3)

    def test_mixed_temperatures(self):
        temperatures = [-10, 5, -3, 8]
        self.assertEqual(closest_to_zero(temperatures), -3)

    def test_equal_temperatures(self):
        temperatures = [2, 2, -2, -2]
        self.assertEqual(closest_to_zero(temperatures), 2)

    def test_zero_temperature(self):
        temperatures = [0]
        self.assertEqual(closest_to_zero(temperatures), 0)


if __name__ == '__main__':
    unittest.main()
