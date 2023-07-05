import unittest

from find_cheating_couples import find_cheating_couples


class TestCheatingCouples(unittest.TestCase):
    def test_example_1(self):
        n = 3
        relationships = [(1, 2), (2, 3), (1, 4)]
        self.assertEqual(find_cheating_couples(n, relationships), 1)

    def test_example_2(self):
        n = 4
        relationships = [(1, 2), (3, 1), (3, 5), (2, 4)]
        self.assertEqual(find_cheating_couples(n, relationships), 2)


if __name__ == '__main__':
    unittest.main()
