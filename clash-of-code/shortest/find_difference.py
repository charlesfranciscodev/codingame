# Function to find the difference between maximum and minimum values in a sequence
def find_difference(n, sequence):
    # Find the maximum and minimum values in the sequence
    max_val = max(sequence)
    min_val = min(sequence)

    # Calculate the difference
    difference = max_val - min_val

    return difference


# Input reading
n = int(input())
sequence = list(map(int, input().split()))

# Output the result
result = find_difference(n, sequence)
print(result)
