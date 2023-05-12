# Unary

## Code Description

The provided code consists of two functions: `to_binary` and `to_unary`. These functions are used to convert text between binary and unary representations.

The `to_binary` function takes a string of text as input and converts each character into its corresponding binary representation. It iterates over each character in the input text, retrieves its ASCII value using the `ord()` function, and formats the ASCII value as a binary string with a width of 7 digits using the `format()` method. The binary representations of all characters are then concatenated to form a binary string, which is returned as the output.

The `to_unary` function takes a binary string as input and converts it into a unary representation. It initializes an empty string for the unary representation and a boolean variable `prev_digit` to keep track of the previous digit encountered. The function handles the first character separately by checking if it is "0" or "1" and adding the corresponding unary representation to the output string. It also updates the `prev_digit` variable accordingly.

For the subsequent characters, the function iterates over the input string starting from the second character. If the current digit is "0" and the previous digit was "1", it adds the unary representation for switching from "1" to "0" to the output string and updates the `prev_digit` variable to `False`. If the current digit is "1" and the previous digit was "0", it adds the unary representation for switching from "0" to "1" to the output string and updates the `prev_digit` variable to `True`. If the current digit is the same as the previous digit, it adds the unary representation for repeating the digit to the output string.

Finally, the function returns the unary representation of the input binary string.

The main part of the code prompts the user to enter a text string, which is then passed through the `to_binary` function to obtain the binary representation. The binary representation is then passed to the `to_unary` function to get the unary representation. Finally, the unary representation is printed as output.

## Code Example

This code provides two functions, `to_binary` and `to_unary`, that allow for the conversion of text between binary and unary representations.

### `to_binary(text) -> str`

This function takes a `text` string as input and converts it into a binary representation.

#### Parameters

- `text` (str): The input text to be converted.

#### Returns

- `binary_text` (str): The binary representation of the input text.

#### Example

```python
text = "A"
binary_text = to_binary(text)
print(binary_text)
```

Output:
```
1000001
```

### `to_unary(text) -> str`

This function takes a `text` string in binary format as input and converts it into a unary representation.

#### Parameters

- `text` (str): The binary representation of the input text.

#### Returns

- `unary_text` (str): The unary representation of the input text.

#### Example

```python
text = "1000011"
unary_text = to_unary(text)
print(unary_text)
```

Output:
```
0 0 00 0000 0 00
```
