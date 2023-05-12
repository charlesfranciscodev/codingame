import unittest

from unary import to_binary
from unary import to_unary


class TestToBinary(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(to_binary(""), "")

    def test_single_character(self):
        self.assertEqual(to_binary("A"), "1000001")
        self.assertEqual(to_binary("a"), "1100001")
        self.assertEqual(to_binary("5"), "0110101")

    def test_multiple_characters(self):
        self.assertEqual(to_binary("Hello"), "10010001100101110110011011001101111")
        self.assertEqual(to_binary("World!"), "101011111011111110010110110011001000100001")


class TestToUnary(unittest.TestCase):
    def test_single_character(self):
        self.assertEqual(to_unary(to_binary("C")), "0 0 00 0000 0 00")
        self.assertEqual(to_unary(to_binary("%")), "00 0 0 0 00 00 0 0 00 0 0 0")

    def test_multiple_characters(self):
        self.assertEqual(to_unary(to_binary("CC")), "0 0 00 0000 0 000 00 0000 0 00")
        self.assertEqual(
            to_unary(to_binary("Chuck Norris' keyboard has 2 keys: 0 and white space.")),
            "0 0 00 0000 0 0000 00 0 0 0 00 000 0 000 00 0 0 0 00 0 0 000 00 000 0 0000 00 0 0 0 00 0 0 00 00 0 0 0 00 00000 0 0 00 00 0 000 00 0 0 00 00 0 0 0000000 00 00 0 0 00 0 0 000 00 00 0 0 00 0 0 00 00 0 0 0 00 00 0 0000 00 00 0 00 00 0 0 0 00 00 0 000 00 0 0 0 00 00000 0 00 00 0 0 0 00 0 0 0000 00 00 0 0 00 0 0 00000 00 00 0 000 00 000 0 0 00 0 0 00 00 0 0 000000 00 0000 0 0000 00 00 0 0 00 0 0 00 00 00 0 0 00 000 0 0 00 00000 0 00 00 0 0 0 00 000 0 00 00 0000 0 0000 00 00 0 00 00 0 0 0 00 000000 0 00 00 00 0 0 00 00 0 0 00 00000 0 00 00 0 0 0 00 0 0 0000 00 00 0 0 00 0 0 00000 00 00 0 0000 00 00 0 00 00 0 0 000 00 0 0 0 00 00 0 0 00 000000 0 00 00 00000 0 0 00 00000 0 00 00 0000 0 000 00 0 0 000 00 0 0 00 00 00 0 0 00 000 0 0 00 00000 0 000 00 0 0 00000 00 0 0 0 00 000 0 00 00 0 0 0 00 00 0 0000 00 0 0 0 00 00 0 00 00 00 0 0 00 0 0 0 00 0 0 0 00 00000 0 000 00 00 0 00000 00 0000 0 00 00 0000 0 000 00 000 0 0000 00 00 0 0 00 0 0 0 00 0 0 0 00 0 0 000 00 0",
        )


if __name__ == "__main__":
    unittest.main()
