import unittest

from count_even_letters import count_even_ascii_letters


class TestCountEvenAsciiLetters(unittest.TestCase):
    def test_no_even_ascii_letters(self):
        result = count_even_ascii_letters("Hello World!")
        self.assertEqual(result, 6)

    def test_one_even_ascii_letter(self):
        result = count_even_ascii_letters("aC")
        self.assertEqual(result, 0)

    def test_multiple_even_ascii_letters(self):
        result = count_even_ascii_letters("AbCdEf")
        self.assertEqual(result, 3)

    def test_empty_sentence(self):
        result = count_even_ascii_letters("")
        self.assertEqual(result, 0)

    def test_only_non_alphabetic_characters(self):
        result = count_even_ascii_letters("123!@#")
        self.assertEqual(result, 0)

    def test_mixed_sentence(self):
        result = count_even_ascii_letters("a1b2C3d4E5f6")
        self.assertEqual(result, 3)


if __name__ == "__main__":
    unittest.main()
