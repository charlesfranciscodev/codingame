import unittest

from extended_fibonacci import extended_fibonacci


class TestExtendedFibonacci(unittest.TestCase):
    def test_positive_index(self):
        self.assertEqual(extended_fibonacci(4), 3)

    def test_negative_index(self):
        self.assertEqual(extended_fibonacci(-4), -3)

    def test_zero_index(self):
        self.assertEqual(extended_fibonacci(0), 0)


if __name__ == "__main__":
    unittest.main()
