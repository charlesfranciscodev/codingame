def separate_upper_lower(text):
    uppercase_chars = ""
    lowercase_chars = ""

    for char in text:
        if char.isupper():
            uppercase_chars += char
        elif char.islower():
            lowercase_chars += char

    return uppercase_chars, lowercase_chars

# Read input
text = input().strip()

# Separate uppercase and lowercase characters
uppercase_chars, lowercase_chars = separate_upper_lower(text)

# Print the results
print(uppercase_chars)
print(lowercase_chars)
