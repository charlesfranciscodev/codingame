# Blunder - Episode 3

Blunder is excited because numerous CodinGamers have re-programmed his natural behavior. However, the issue is that these programs have varying execution times, making it challenging for Blunder to fully enjoy his inactivity. Your task is to determine the most likely computational complexity of the programs used to re-program Blunder based on their performance measures. The performance measures are recorded for the execution time of the programs with different volumes of data.

## Input

- Line 1: an integer N, which represents the number of performance measures carried out on the same program.
- N following lines: Each line contains two integers, num and t. Num represents the number of items that the program has processed, and t represents the execution time measured to process these items in microseconds. These values are separated by a space. Values of num are unique and sorted in ascending order.

## Output

- Your program should output the most probable computational complexity among the following possibilities: O(1), O(log n), O(n), O(n log n), O(n^2), O(n^2 log n), O(n^3), O(2^n).

## Constraints

- 5 < N < 1000
- 5 < num < 15000
- 0 < t < 10000000

## Solution Summary

To determine the most likely computational complexity, we need to analyze the performance measures and identify the pattern in execution times. The computational complexities we need to consider are O(1), O(log n), O(n), O(n log n), O(n^2), O(n^2 log n), O(n^3), and O(2^n).

We can analyze the performance measures by calculating the ratio of execution time t for consecutive values of num. The complexity can be inferred from the behavior of this ratio:

- If the ratio is approximately constant, it suggests O(1) complexity.
- If the ratio increases logarithmically, it suggests O(log n) complexity.
- If the ratio increases linearly, it suggests O(n) complexity.
- If the ratio increases linearithmically, it suggests O(n log n) complexity.
- If the ratio increases quadratically, it suggests O(n^2) complexity.
- If the ratio increases n log n times, it suggests O(n^2 log n) complexity.
- If the ratio increases cubically, it suggests O(n^3) complexity.
- If the ratio increases exponentially, it suggests O(2^n) complexity.

By analyzing the ratios for each pair of consecutive measurements, we can make an educated guess about the most likely computational complexity.