import unittest

from sum_natural_numbers import find_output


class TestFindOutputFunction(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(find_output(5), 15)

    def test_case_2(self):
        self.assertEqual(find_output(7), 28)

    def test_case_3(self):
        self.assertEqual(find_output(8), 36)

    def test_case_4(self):
        self.assertEqual(find_output(1), 1)

    def test_case_5(self):
        self.assertEqual(find_output(9), 45)

    def test_case_6(self):
        self.assertEqual(find_output(10), 55)

    def test_case_7(self):
        self.assertEqual(find_output(2), 3)

    def test_case_8(self):
        self.assertEqual(find_output(3), 6)

    def test_case_9(self):
        self.assertEqual(find_output(4), 10)

    def test_case_10(self):
        self.assertEqual(find_output(6), 21)


if __name__ == "__main__":
    unittest.main()
