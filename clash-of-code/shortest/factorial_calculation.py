def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def calculate_result(X, N):
    x_factorial = factorial(X)
    x_minus_n_factorial = factorial(X - N)
    result = x_factorial // x_minus_n_factorial
    return result

# Taking input
X = int(input())
N = int(input())

# Calculating and printing the result
output = calculate_result(X, N)
print(output)
