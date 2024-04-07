# Valid Code Combinations

## Problem Description

This code calculates the number of unique combinations possible based on certain criteria applied to a given input string. The input string consists of digits, and the code filters out the digits greater than 4. Then, it calculates the number of unique digits in the filtered list. Finally, it computes the number of unique combinations of these valid digits.

## Code

- When the script is executed directly, it prompts the user to input a string of digits.
- It then calls the `count_valid_codes` function to count the valid digits in the input string.
- Next, it calls the `calculate_combinations` function with the count of valid digits.
- Finally, it prints the result.

## Example

```
Input: 123456
Output: 60
```
