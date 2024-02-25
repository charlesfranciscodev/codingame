import unittest

from harshad_number import is_harshad_number


class TestHarshadNumber(unittest.TestCase):
    def test_harshad_number(self):
        # Test cases with Harshad numbers
        self.assertTrue(is_harshad_number(18))  # 1 + 8 = 9, 18 is divisible by 9
        self.assertTrue(is_harshad_number(20))  # 2 + 0 = 2, 20 is divisible by 2
        self.assertTrue(is_harshad_number(81))  # 8 + 1 = 9, 81 is divisible by 9

        # Test cases with non-Harshad numbers
        self.assertFalse(is_harshad_number(37))  # 3 + 7 = 10, 37 is not divisible by 10
        self.assertFalse(is_harshad_number(99))  # 9 + 9 = 18, 99 is not divisible by 18


if __name__ == "__main__":
    unittest.main()
