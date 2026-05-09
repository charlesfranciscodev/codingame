# ASCII Art

## Description

The goal of this puzzle is to simulate an old airport terminal display by displaying a line of text in ASCII art. To solve this challenge, you'll learn how to manage strings and perform array arithmetics. You will practice splitting strings into separate parts, concatenating them into a new string, and using array indexes effectively. By leveraging data structures like arrays or hash tables, you can store and recreate strings to create the ASCII art representation of the input text.

## Example Input/Output

**Input**

```
4
5
CodinGame
 #  ##   ## ##  ### ###  ## # # ###  ## # # #   # # ###  #  ##   #  ##   ## ### # # # # # # # # # # ### ### 
# # # # #   # # #   #   #   # #  #    # # # #   ### # # # # # # # # # # #    #  # # # # # # # # # #   #   # 
### ##  #   # # ##  ##  # # ###  #    # ##  #   ### # # # # ##  # # ##   #   #  # # # # ###  #   #   #   ## 
# # # # #   # # #   #   # # # #  #  # # # # #   # # # # # # #    ## # #   #  #  # # # # ### # #  #  #       
# # ##   ## ##  ### #    ## # # ###  #  # # ### # # # #  #  #     # # # ##   #  ###  #  # # # #  #  ###  #  

```

**Output**

```
 ##  #  ##  ### ###  ##  #  # # ### 
#   # # # #  #  # # #   # # ### #   
#   # # # #  #  # # # # ### ### ##  
#   # # # #  #  # # # # # # # # #   
 ##  #  ##  ### # #  ## # # # # ### 
```

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

## Code Example

```python
L = int(input())  # width of each character
H = int(input())  # height of the ASCII art
T = input()  # input text to be converted to ASCII art

# Read the ASCII art for A-Z and '?'
ascii_art = []
for i in range(H):
    row = input()
    ascii_art.append(row)

# Create a dictionary to store the ASCII art for each character
ascii_dict = {}

for i in range(26):  # for A-Z
    ascii_dict[chr(i + ord('A'))] = [ascii_art[j][i*L:(i+1)*L] for j in range(H)]

# '?' will represent any unknown character
ascii_dict['?'] = [ascii_art[j][26*L:(27)*L] for j in range(H)]

# Convert the input text T to uppercase and handle unknown characters
result = ['' for _ in range(H)]
for char in T:
    if char.isalpha():
        char = char.upper()
    else:
        char = '?'
    
    for i in range(H):
        result[i] += ascii_dict.get(char, ascii_dict['?'])[i]

# Print the ASCII art for the input text T
for line in result:
    print(line)

```

## Explanation of Code Steps

1. **Input Parsing**:
   - Read `L` (width of each letter), `H` (height of letters), and `T` (input text).
   - For `H` lines, read the ASCII art representing all characters from A to Z and `?`.

2. **Store ASCII Art**:
   - Use a list to store the ASCII art of each character in a structured way.
   - For each character in the string `T`, extract the corresponding ASCII art from this list.

3. **Handle Non-alphabet Characters**:
   - Any character outside of the range `[A-Z]` or `[a-z]` should be replaced by the `?` character's ASCII art.

4. **Print the ASCII Art**:
   - For each line in the height `H`, concatenate and print the corresponding parts of the ASCII art for each character in `T`.

## Edge Cases

Test your program by experimenting with an empty ASCII art representation for one or more characters to confirm that it appropriately manages missing character representations. Additionally, try inputting a combination of uppercase and lowercase letters to verify that the program handles case conversion and character lookup accurately. Test different combinations of widths and heights to ensure the program can handle various dimensions without errors or output distortion. Provide a single character input string to assess the program's handling of single-character input and its corresponding ASCII art output. Furthermore, examine input strings containing leading, trailing, and multiple consecutive whitespace characters to ensure proper whitespace handling. In summary, thoroughly test your program with various inputs, including empty ASCII art, mixed case letters, different dimensions, single characters, and strings with whitespace, to ensure it handles all cases accurately.
