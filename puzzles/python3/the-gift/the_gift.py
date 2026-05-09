def calculate_contributions(N, C, budgets):
    budgets.sort()
    total_budget = sum(budgets)

    if total_budget < C:
        return None

    contributions = []
    remaining_budget = C

    for budget in budgets[:-1]:
        contribution = min(budget, remaining_budget // (N - len(contributions)))
        contributions.append(contribution)
        remaining_budget -= contribution
    contributions.append(remaining_budget)  # Last person pays the remaining budget

    return sorted(contributions)


if __name__ == "__main__":
    # Read input
    N = int(input())
    C = int(input())

    budgets = []
    for _ in range(N):
        budget = int(input())
        budgets.append(budget)

    # Calculate contributions
    result = calculate_contributions(N, C, budgets)

    # Print output
    if result:
        for contribution in result:
            print(contribution)
    else:
        print("IMPOSSIBLE")
