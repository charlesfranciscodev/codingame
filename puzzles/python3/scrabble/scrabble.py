from typing import Dict, List


# letter => points
MAPPING: Dict[str, int] = {
    'e': 1, 'a': 1, 'i': 1, 'o': 1, 'n': 1, 'r': 1, 't': 1, 'l': 1, 's': 1, 'u': 1,
    'd': 2, 'g': 2,
    'b': 3, 'c': 3, 'm': 3, 'p': 3,
    'f': 4, 'h': 4, 'v': 4, 'w': 4, 'y': 4,
    'k': 5,
    'j': 8, 'x': 8,
    'q': 10, 'z': 10,
}


def is_valid_word(word: List[str], letters: List[str]) -> bool:
    for c in word:
        if c not in letters:
            return False
        else:
            letters.remove(c)
    return True


def calculate_score(word) -> int:
    total_score = 0
    for c in word:
        total_score += MAPPING[c]
    return total_score


def solve(words, letters: str) -> str:
    best_score = 0
    best_word = ""
    for word in words:
        letters_copy: List[str] = list(letters)
        if is_valid_word(word, letters_copy):
            current_score = calculate_score(word)
            if current_score > best_score:
                best_score = current_score
                best_word = word
    return best_word


if __name__ == "__main__":
    # read game input
    words: List[str] = []
    nb_words = int(input())
    for _ in range(nb_words):
        words.append(input())
    letters = input()

    print(solve(words, letters))
