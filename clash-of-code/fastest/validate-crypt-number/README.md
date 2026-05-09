# Cryptichips

## Description

You've invented a new type of payment system, Cryptichips. Like a credit card, each Cryptichip has a unique number and uses the "Fuhn Algorithm" to validate the number.

The validation is as follows:
- The number must be 13 digits long (ignore spaces)
- The last digit must be ( the sum of each of the first 12 digits * the 1-based index of the digit) mod 10

## Example

For valid number 5534 5132 1123 5
Then last digit (5) is calculated as follows:

```
(1*5 + 2*5 + 3*3 + 4*4 + 5*5 + 6*1 + 7*3 + 8*2 + 9*1 + 10*1 + 11*2 + 12*3) % 10
185 % 10 = 5
```
