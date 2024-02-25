def maximum_gold(m, n, k, grid):
    max_gold = 0

    for i in range(0, m, k):
        for j in range(0, n, k):
            gold_sum = 0

            for x in range(i, i + k):
                for y in range(j, j + k):
                    gold_sum += grid[x][y]

            max_gold = max(max_gold, gold_sum)

    return max_gold


# Read input
m, n, k = map(int, input().split())
grid = []
for _ in range(m):
    row = list(map(int, input().split()))
    grid.append(row)

# Call the function and print the result
result = maximum_gold(m, n, k, grid)
print(result)
