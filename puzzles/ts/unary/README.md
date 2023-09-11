# Unary

## Summary

The goal of this program is to encode an incoming message using a special binary encoding method. In this method, the input message, consisting of ASCII characters, is transformed into blocks of 0s separated by spaces. The first block is either 0 or 00, where 0 represents a series of 1s and the absence of 0 represents a series of 0s. The second block contains the number of 0s corresponding to the number of bits in the series. For example, the character 'C' is encoded as "0 0 00 0000 0 00," where 'C' in binary is 1000011. The program should handle input messages with up to 100 ASCII characters and output the encoded message accordingly.

## Documentation

### toBinary(message: string): string
This function takes a `message` as input, which is a string, and converts each character of the message into its binary representation. It iterates over each character of the message using a `for...of` loop and appends the binary representation of each character to the `binary` variable. The binary representation of each character is obtained using the `charCodeAt(0)` method, which returns the Unicode value of the character, and then converted to a binary string using the `toString(2)` method. The resulting binary strings are padded with leading zeros using the `padStart()` method to ensure that each binary representation has a length of 7. Finally, the function returns the concatenated binary string.

### toUnary(binary: string): string
This function takes a `binary` string as input, which represents a binary sequence, and converts it into a unary representation. It initializes an empty array called `allSeries` to store the unary sequences. The function uses a regular expression (`/(.)\1*/g`) with the `match()` method to find consecutive groups of the same character in the binary string. The `groups` variable holds an array of these consecutive groups. For each group, the function creates a unary series based on the first character of the group. If the first character is '1', the first block of the unary series is set to "0"; otherwise, it is set to "00". The second block of the unary series is set to a sequence of '0' characters that has the same length as the group. The first and second blocks are concatenated with a space in between, and the resulting series is added to the `allSeries` array. Finally, the function joins all the unary series in the `allSeries` array into a single string separated by spaces and returns it.

The remaining code after the function definitions reads input from the user using `readline()`, assigns it to the `message` variable, and then calls the `toBinary()` function to convert the message to binary. The resulting binary string is stored in the `binary` variable. After that, the `toUnary()` function is called with the `binary` string as input to convert it into a unary representation. The resulting unary string is stored in the `unary` variable. Finally, the unary string is printed to the console using `console.log()`.

Please note that this code assumes the presence of some I/O functionality, such as the `readline()` function, which might not be available in all JavaScript environments.
