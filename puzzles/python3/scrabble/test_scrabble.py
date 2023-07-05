import unittest

from scrabble import calculate_score, find_max_score_word


class ScrabbleSolverTests(unittest.TestCase):
    def setUp(self):
        self.LETTER_POINTS = {
            'e': 1, 'a': 1, 'i': 1, 'o': 1, 'n': 1, 'r': 1, 't': 1, 'l': 1, 's': 1, 'u': 1,
            'd': 2, 'g': 2,
            'b': 3, 'c': 3, 'm': 3, 'p': 3,
            'f': 4, 'h': 4, 'v': 4, 'w': 4, 'y': 4,
            'k': 5,
            'j': 8, 'x': 8,
            'q': 10, 'z': 10,
        }

    def test_calculate_score(self):
        word = "banana"
        score = calculate_score(word, self.LETTER_POINTS)
        self.assertEqual(score, 8)

    def test_find_max_score_word_with_single_solution(self):
        dictionary = ["hello", "world", "python", "openai"]
        letters = "owlrd"
        max_score_word = find_max_score_word(dictionary, letters, self.LETTER_POINTS)
        self.assertEqual(max_score_word, "world")

    def test_find_max_score_word_with_different_scores(self):
        dictionary = ["cat", "hat", "dog"]
        letters = "atdoh"
        max_score_word = find_max_score_word(dictionary, letters, self.LETTER_POINTS)
        self.assertEqual(max_score_word, "hat")

    def test_find_max_score_word_duplicate_letters(self):
        dictionary = ["arrest", "rarest", "raster", "raters", "sartre", "starer", "waster", "waters", "wrest", "wrase"]
        letters = "arwtsre"
        max_score_word = find_max_score_word(dictionary, letters, self.LETTER_POINTS)
        self.assertEqual(max_score_word, "waster")

    def test_find_max_score_word_value_better_than_size(self):
        dictionary = ["entire", "tween", "soft", "would", "test"]
        letters = "etiewrn"
        max_score_word = find_max_score_word(dictionary, letters, self.LETTER_POINTS)
        self.assertEqual(max_score_word, "tween")


if __name__ == "__main__":
    unittest.main()
