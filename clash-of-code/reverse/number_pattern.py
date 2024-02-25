import unittest


def reverse_game(input_num):
    return int(input_num * 1.5)


class TestReverseGame(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(reverse_game(1), 1)

    def test_case_2(self):
        self.assertEqual(reverse_game(2), 3)

    def test_case_3(self):
        self.assertEqual(reverse_game(5), 7)

    def test_case_4(self):
        self.assertEqual(reverse_game(100), 150)


if __name__ == "__main__":
    unittest.main()
