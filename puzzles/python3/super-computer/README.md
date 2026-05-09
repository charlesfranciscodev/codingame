# Super Computer

## Problem Description

You are tasked with scheduling calculations on a supercomputer in the Computer2000 data center. Scientists provide you with the starting day and duration of their calculations. Your goal is to maximize the number of calculations that can be carried out without overlapping reservation periods.

### Rules

- Scientists provide their calculations with the following information:
  - Calculation name (not used in calculations)
  - Starting day of the calculation (an integer)
  - Duration (number of consecutive days required for the calculation)

- Calculations are scheduled in consecutive days without gaps.

- The goal is to maximize the number of calculations that can be carried out.

- Calculations cannot overlap in their reservation periods.

- Calculate the maximum number of non-overlapping calculations that can be performed.

### Example

Given the following input:

```
4
2 5
9 7
15 6
9 3
```

- Calculation A starts on day 2 and ends on day 6.
- Calculation B starts on day 9 and ends on day 15.
- Calculation C starts on day 15 and ends on day 20.
- Calculation D starts on day 9 and ends on day 11.

In this example, it's not possible to carry out all the calculations because the periods for B and C overlap. The maximum number of calculations that can be carried out is 3: A, D, and C.

## Solution Summary

To solve this problem, you need to find the maximum number of non-overlapping calculations that can be performed. Here's a high-level summary of the solution:

1. Read the input, including the number of calculations (N) and the details of each calculation (starting day and duration).

2. Sort the calculations based on their ending days in ascending order. This step ensures that we prioritize calculations with earlier ending days.

3. Initialize variables to keep track of the current end day and the count of performed calculations.

4. Iterate through the sorted calculations. For each calculation:
   - If its starting day is after the current end day, it can be performed. Increment the count and update the current end day to the end day of the performed calculation.

5. Output the count of performed calculations as the maximum number of calculations that can be carried out without overlapping.

This algorithm ensures that calculations are scheduled in a way that maximizes the usage of the supercomputer without overlapping reservation periods.

## Example Code

```python
# Sort the calculations
calculations.sort(key=lambda x: x[1])

# Initialize variables
max_calculations = 0
selected_calculations = []

# Greedy algorithm
for calculation in calculations:
    if not selected_calculations:
        selected_calculations.append(calculation)
        max_calculations += 1
    elif calculation[0] > selected_calculations[-1][1]:
        selected_calculations.append(calculation)
        max_calculations += 1
```
