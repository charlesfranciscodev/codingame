from collections import Counter
from typing import Dict
from typing import List
from typing import Optional


def calculate_score(word: str, LETTER_POINTS: Dict[str, int]) -> int:
    score = 0
    for letter in word:
        score += LETTER_POINTS.get(letter, 0)
    return score


def find_max_score_word(dictionary: List[str], letters: str, LETTER_POINTS: Dict[str, int]) -> Optional[str]:
    max_score = 0
    max_score_word = None

    for word in dictionary:
        # Check if the word can be formed using the available letters
        letters_counter = Counter(letters)
        word_counter = Counter(word)
        if all(letters_counter[letter] >= count for letter, count in word_counter.items()):
            score = calculate_score(word, LETTER_POINTS)
            if score > max_score:
                max_score = score
                max_score_word = word

    return max_score_word


LETTER_POINTS = {
    "e": 1,
    "a": 1,
    "i": 1,
    "o": 1,
    "n": 1,
    "r": 1,
    "t": 1,
    "l": 1,
    "s": 1,
    "u": 1,
    "d": 2,
    "g": 2,
    "b": 3,
    "c": 3,
    "m": 3,
    "p": 3,
    "f": 4,
    "h": 4,
    "v": 4,
    "w": 4,
    "y": 4,
    "k": 5,
    "j": 8,
    "x": 8,
    "q": 10,
    "z": 10,
}


if __name__ == "__main__":
    # Input
    N = int(input())
    dictionary = [input() for _ in range(N)]
    letters = input()

    # Output
    result = find_max_score_word(dictionary, letters, LETTER_POINTS)
    print(result)
