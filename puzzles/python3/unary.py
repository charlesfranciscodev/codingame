def to_binary(text) -> str:
    binary_text = ""
    for character in text:
        binary_text += "{0:{fill}7b}".format(ord(character), fill="0")
    return binary_text


def to_unary(text) -> str:
    unary_text = ""
    prev_digit = False  # False = 0, True = 1
    # handle first character
    if len(text) >= 1:
        if text[0] == "0":
            unary_text += "00 0"
        else:
            unary_text += "0 0"
            prev_digit = True

    for i in range(1, len(text)):
        if text[i] == "0" and prev_digit:
            unary_text += " 00 0"  # switch from 1 to 0
            prev_digit = False
        elif text[i] == "1" and not prev_digit:
            unary_text += " 0 0"  # switch from 0 to 1
            prev_digit = True
        else:
            unary_text += "0"  # repeat digit
    return unary_text


if __name__ == "__main__":
    text = input()
    binary_text = to_binary(text)
    unary_text = to_unary(binary_text)
    print(unary_text)
