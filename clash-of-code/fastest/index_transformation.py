# Read input
A = int(input())
L = list(map(int, input().split()))

# Initialize an empty result list
result = []

# Iterate through each number in the list
for num in L:
    result.append(L[num])  # Append the number at the index given by 'num'

# Print the result as space-separated values
print(" ".join(map(str, result)))
