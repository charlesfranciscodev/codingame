# Read input values
M = int(input())
N = int(input())
numbers = list(map(int, input().split()))

# Calculate the sum of mods
mod_sum = sum(num % M for num in numbers)

# Print the result
print(mod_sum)
