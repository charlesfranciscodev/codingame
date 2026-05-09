def generate_pattern(n, char):
    for i in range(n):
        spaces = " " * (n - i - 1)
        pattern = char * (2 * i + 1)
        print(spaces + pattern)


# Read input
n = int(input())
char = input()

# Generate and print the pattern
generate_pattern(n, char)
