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

## High-Level Strategy

1. **Calculate Ratios:**
   - Iterate through the provided performance measures.
   - Calculate the ratio of execution time (t) between consecutive measurements.
   - Ratios are calculated as t[i] / t[i-1] for each pair of consecutive measurements.

2. **Analyze Ratios:**
   - Identify patterns in the calculated ratios.
   - Different computational complexities exhibit distinct patterns in how the execution time grows with increasing input size.

3. **Match Patterns to Complexity:**
   - Associate observed patterns with the most likely computational complexities:
     - Constant ratio suggests O(1) complexity.
     - Logarithmic increase suggests O(log n) complexity.
     - Linear increase suggests O(n) complexity.
     - Linearithmic increase suggests O(n log n) complexity.
     - Quadratic increase suggests O(n^2) complexity.
     - Linearithmic increase multiplied by n suggests O(n^2 log n) complexity.
     - Cubic increase suggests O(n^3) complexity.
     - Exponential increase suggests O(2^n) complexity.

4. **Select Most Probable Complexity:**
   - Based on the observed patterns, determine the most probable computational complexity among the given possibilities.

This high-level strategy involves analyzing the growth patterns of execution times to infer the underlying computational complexity. It allows us to make educated guesses about the nature of the algorithms used in re-programming Blunder, providing insights into the efficiency of the implemented solutions.
