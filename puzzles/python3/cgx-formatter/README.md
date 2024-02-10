# CGX Formatter

## Overview

At CodinGame, we've introduced a new text data format called CGX to represent structured information. CGX content consists of ELEMENTs, which can be of various types such as BLOCK, PRIMITIVE_TYPE, or KEY_VALUE. Your task is to write a program that formats CGX content to enhance readability according to the specified rules.

## How to Play

1. **Input**: 
   - Line 1: An integer N representing the number of CGX lines to be formatted.
   - The next N lines contain the CGX content, each line having a maximum of 1000 ASCII characters.

2. **Output**:
   - The formatted CGX content adhering to the given rules.

3. **Constraints**:
   - The number of CGX lines, N, lies between 0 and 10000.
   - The CGX content provided will always be valid.

4. **Rules for Formatting**:
   - The displayed result should not contain any space, tab, or carriage return.
   - The content of strings of characters must not be modified.
   - A BLOCK starts on its own line.
   - The markers at the start and end of a BLOCK are in the same column.
   - Each ELEMENT within a BLOCK is indented 4 spaces from the marker of that BLOCK.
   - A KEY_VALUE starts on its own line.
   - A PRIMITIVE_TYPE starts on its own line unless it is the value of a KEY_VALUE.

## Conclusion

Get ready to dive into formatting CGX content efficiently! Your goal is to write a program that takes CGX content as input and outputs the properly formatted version following the specified rules. Good luck!
