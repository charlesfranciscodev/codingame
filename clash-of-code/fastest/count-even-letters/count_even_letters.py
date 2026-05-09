def count_even_ascii_letters(sentence):
    count = 0
    for c in sentence:
        if c.isalpha():
            ascii_value = ord(c)
            if ascii_value % 2 == 0:
                count += 1

    return count


if __name__ == "__main__":
    sentence = input().strip()
    result = count_even_ascii_letters(sentence)
    print(result)
