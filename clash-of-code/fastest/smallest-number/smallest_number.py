def get_smallest_number(N):
    # Function to calculate the sum of digits in a number
    def sum_of_digits(num):
        return sum(int(digit) for digit in str(num))

    # Start searching for M from 1
    M = 1

    while True:
        # Calculate the sum of digits of N and M
        sum_N = sum_of_digits(N)
        sum_M = sum_of_digits(M)

        # Check if the condition is satisfied
        if sum_N + sum_M == abs(N - M):
            return M

        # Increment M for the next iteration
        M += 1


# Get input from the user
N = int(input())

# Call the function to get the smallest number M
result = get_smallest_number(N)

# Print the result
print(result)
