import unittest

from square_root import find_square_root


class TestFindSquareRoot(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(find_square_root(5, [17, 9, 4, 6, 25]), 10)

    def test_case_2(self):
        self.assertEqual(find_square_root(0, []), 0)

    def test_case_3(self):
        self.assertEqual(find_square_root(3, [0, 0, 0]), 0)

    def test_case_4(self):
        self.assertEqual(find_square_root(4, [8, 8, 8, 8]), 8)

    def test_case_5(self):
        self.assertEqual(find_square_root(2, [1, 1000]), 31)

    def test_case_6(self):
        self.assertEqual(find_square_root(1, [42]), 42)


if __name__ == "__main__":
    unittest.main()
