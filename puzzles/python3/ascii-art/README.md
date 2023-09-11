# ASCII Art

## Description

"ASCII Art" is a beginner-level coding challenge available on the CodinGame platform. In this challenge, the player is given a string of characters and a font size, and is asked to generate an ASCII art representation of the string using ASCII characters.

The ASCII art output should be a sequence of lines, each line representing a row of the output. Each row should contain the ASCII characters that correspond to the input string, with each character expanded to the specified font size. If a character in the input string is not a letter or cannot be represented in ASCII art, it should be replaced with a question mark.

The challenge consists of writing a program that takes as input the string of characters, the font size, and the ASCII art characters to be used for each letter, and outputs the corresponding ASCII art representation.

The challenge is designed to help players learn and practice programming skills such as string manipulation, input/output handling, and ASCII art rendering. It is a fun and engaging way to improve programming skills while solving a challenging and entertaining puzzle.

## Problem Approach

To solve this coding puzzle, you'll need to create a program that takes the width (L), height (H), text (T), and character representations (ASCII art) for letters A-Z and '?'. Here's a high-level outline of how you can approach this problem:

1. **Input Parsing**:
   - Read the values of L, H, and T from the input.
   - Read the ASCII art representations of characters A-Z and '?' and store them in a data structure for easy access.

2. **Prepare Data Structures**:
   - You can use dictionaries or arrays to store the ASCII art for each character. For example, you might create a dictionary where the keys are characters (A-Z, '?') and the values are lists of strings representing their ASCII art.

3. **Iterate Through Text (T)**:
   - For each character in the input text T:
     - Check if it's an uppercase letter (A-Z).
     - If it's a lowercase letter (a-z), convert it to uppercase for lookup.
     - If it's not an uppercase letter or a valid character (not in [a-z] or [A-Z]), use the '?' character's ASCII art.
     - Retrieve the ASCII art representation for the character from your data structure.

4. **Print the ASCII Art**:
   - For each line of the ASCII art representation of the characters:
     - Concatenate the corresponding lines for each character in T.
     - Print the resulting line.

5. **Repeat for Each Line**:
   - Repeat steps 3 and 4 for each line of the ASCII art (there will be H lines).

6. **Handle Output**:
   - Print the entire ASCII art representation for the input text T.

7. **Testing**:
   - Test your program with different input cases, including different widths, heights, and text inputs, to ensure it works correctly.

Here's a simplified Python-like pseudocode for the main part of the code:

```python
# Input parsing
L = int(input())
H = int(input())
T = input()
char_art = {}  # Dictionary to store character ASCII art

# Populate char_art with ASCII art representations for A-Z and '?'

# Process and print the ASCII art for each line
for i in range(H):
    line = ""  # Initialize an empty line for each row
    for char in T:
        if 'A' <= char <= 'Z':
            line += char_art[char][i]
        elif 'a' <= char <= 'z':
            line += char_art[char.upper()][i]
        else:
            line += char_art['?'][i]
    print(line)
```

This pseudocode outlines the key steps to solve the coding puzzle. You need to implement the details, including reading the ASCII art representations and handling edge cases.
