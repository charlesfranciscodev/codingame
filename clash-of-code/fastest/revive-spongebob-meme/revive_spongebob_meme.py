def revive_spongebob_meme(input_string):
    converted_string = ""
    i = 0
    for char in input_string:
        if char.isalpha():
            if i % 2 == 0:
                converted_string += char.upper()
            else:
                converted_string += char.lower()
            i += 1
        else:
            converted_string += char
    return converted_string


# Example usage
input_string = input()
output_string = revive_spongebob_meme(input_string)
print(output_string)
