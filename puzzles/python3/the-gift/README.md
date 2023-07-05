# The Gift

## Problem Description

The Pilipius want to offer a present to one of them. They all have different budgets to invest in this present. The goal is to find a fair method that determines the maximum budget each Pilipiu can afford. The Doctor wants to create a program to help solve this problem.

The Doctor has the list of maximum budgets for each Pilipiu. The program should check if it is possible to buy the present and calculate how much each Pilipiu should contribute, according to their respective budget limits.

### Rules

- No Pilipiu can pay more than their maximum budget.
- The optimal solution is the one where the highest contribution is minimal.
- If there are multiple optimal solutions, the best solution is the one where the highest second contribution is minimal, and so on.

### Input

The input consists of the following:

- Line 1: The number `N` of participants.
- Line 2: The price `C` of the gift.
- Next `N` lines: The list of budgets `B` of participants.

### Output

If it is possible to buy the present, the program should output `N` lines, each containing the contribution of a participant, sorted in ascending order. If it is not possible to buy the present, the program should output "IMPOSSIBLE".

### Constraints

- 0 < `N` ≤ 2000
- 0 ≤ `C` ≤ 1000000000
- 0 ≤ `B` ≤ 1000000000

## Solution

The solution can be implemented using a greedy algorithm approach. Here's how the algorithm works:

1. Sort the list of budgets in ascending order.
2. Calculate the total budget by summing up all the budgets.
3. If the total budget is less than the price of the gift, return "IMPOSSIBLE" since it's not possible to buy the present.
4. Initialize an empty list to store the contributions.
5. Iterate over the budgets except for the last one:
   - Calculate the contribution for the current budget by taking the minimum between the budget and the remaining budget divided by the number of participants left.
   - Append the contribution to the list of contributions.
   - Update the remaining budget by subtracting the contribution.
6. Append the remaining budget to the list of contributions since the last person pays the remaining amount.
7. Return the sorted list of contributions.

## Usage

The `calculate_contributions` function can be used to solve the problem. It takes three arguments: `N` (number of participants), `C` (price of the gift), and `budgets` (a list of budgets for each participant). It returns a list of contributions if it is possible to buy the present, or `None` if it is not possible.

```python
contributions = calculate_contributions(N, C, budgets)
if contributions is None:
    print("IMPOSSIBLE")
else:
    for contribution in contributions:
        print(contribution)
```

You can provide the input as described in the problem statement and use the `calculate_contributions` function to calculate the contributions. If the result is not `None`, you can iterate over the contributions and print them. Otherwise, you should output "IMPOSSIBLE".

The provided unit tests in the previous section can be used to verify the correctness of the implementation and ensure that it produces the expected output for different test cases.