def sum_occurrences(N):
    count = 0
    square_N = N ** 2

    for num in range(square_N + 1):
        for digit in str(num): 
            count += str(N).count(str(digit))

    return count

# Example usage
N = int(input())
result = sum_occurrences(N)
print(result)
