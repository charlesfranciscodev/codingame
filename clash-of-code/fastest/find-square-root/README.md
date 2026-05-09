# Square Root of Product Puzzle

## Description

This Python program solves a puzzle that involves finding the square root of the product of the highest and lowest numbers in a given list. If the list is empty (N is 0), the program returns 0.

## Input

- Line 1: An integer N representing the number of integers provided.
- N next lines: Integers A representing the numbers in the list.

## Output

The program outputs the result of the square root of the product of the lowest and the highest numbers in the list, rounded down.

## Constraints

- 0 ≤ N ≤ 100
- 0 ≤ A ≤ 1000

## Example

### Input

```
5
17
9
4
6
25
```

### Output

```
10
```

## How to Use

1. Run the Python script.
2. Enter the number of integers (N).
3. Enter each integer in the list on separate lines.
4. The program will display the result of the square root of the product.

## Unit Tests

The repository includes unit tests to ensure the correctness of the `find_square_root` function. You can run these tests using the `unittest` module.

```bash
python test_puzzle.py
```
