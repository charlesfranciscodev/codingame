import unittest

from the_descent import solve


class TestSolve(unittest.TestCase):
    def test_single_mountain(self):
        mountain_heights = [5]
        expected = 0
        result = solve(mountain_heights)
        self.assertEqual(result, expected)

    def test_equal_heights(self):
        mountain_heights = [3, 3, 3, 3]
        expected = 0
        result = solve(mountain_heights)
        self.assertEqual(result, expected)

    def test_increasing_heights(self):
        mountain_heights = [1, 2, 3, 4, 5]
        expected = 4
        result = solve(mountain_heights)
        self.assertEqual(result, expected)

    def test_decreasing_heights(self):
        mountain_heights = [5, 4, 3, 2, 1]
        expected = 0
        result = solve(mountain_heights)
        self.assertEqual(result, expected)

    def test_random_heights(self):
        mountain_heights = [3, 5, 2, 6, 1, 4]
        expected = 3
        result = solve(mountain_heights)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
