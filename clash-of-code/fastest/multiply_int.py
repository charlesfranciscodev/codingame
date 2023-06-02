m = int(input())  # Read the number of integers to multiply

for _ in range(m):
    n = int(input())  # Read each integer

    if n % 2 == 0:
        result = n * 2  # If n is divisible by 2, multiply by 2
    else:
        result = n * 3  # Otherwise, multiply by 3

    print(result)  # Output the multiplied integer
