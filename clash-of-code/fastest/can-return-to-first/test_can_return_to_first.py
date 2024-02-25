import unittest

from can_return_to_first import can_return_to_first_element


class TestCanReturnToFirstElement(unittest.TestCase):
    def test_returns(self):
        N = 5
        A = [3, 4, 2, 1, 0]
        result = can_return_to_first_element(N, A)
        self.assertEqual(result, "returns")

    def test_cycling(self):
        N = 5
        A = [3, 4, 2, 1, 1]
        result = can_return_to_first_element(N, A)
        self.assertEqual(result, "cycling")

    def test_large_list(self):
        N = 100
        A = list(range(1, N)) + [0]
        result = can_return_to_first_element(N, A)
        self.assertEqual(result, "returns")


if __name__ == "__main__":
    unittest.main()
