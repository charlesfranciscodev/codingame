import unittest

from leetspeak_variants import generate_leetspeak_variants


class TestLeetspeakVariants(unittest.TestCase):
    def test_single_character(self):
        word = "A"
        expected_variants = sorted(["A", "4"])
        self.assertEqual(generate_leetspeak_variants(word), expected_variants)

    def test_word_with_leetspeak_characters(self):
        word = "Hello"
        expected_variants = sorted(
            [
                "H3110",
                "H311o",
                "H31l0",
                "H31lo",
                "H3l10",
                "H3l1o",
                "H3ll0",
                "H3llo",
                "He110",
                "He11o",
                "He1l0",
                "He1lo",
                "Hel10",
                "Hel1o",
                "Hell0",
                "Hello",
            ]
        )
        print(generate_leetspeak_variants(word))
        self.assertEqual(generate_leetspeak_variants(word), expected_variants)

    def test_empty_string(self):
        word = ""
        expected_variants = [""]
        self.assertEqual(generate_leetspeak_variants(word), expected_variants)


if __name__ == "__main__":
    unittest.main()
