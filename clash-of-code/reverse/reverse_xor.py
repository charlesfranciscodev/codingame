import unittest


def find_single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result


class TestFindSingleNumber(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(find_single_number([1, 0, 1]), 0)

    def test_case_2(self):
        self.assertEqual(find_single_number([6, 6, 9]), 9)

    def test_case_3(self):
        self.assertEqual(find_single_number([278, 890, 890]), 278)

    def test_case_4(self):
        self.assertEqual(find_single_number([5, 9, 5]), 9)


if __name__ == "__main__":
    unittest.main()
