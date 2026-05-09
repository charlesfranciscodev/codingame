def generate_matrix(n):
    matrix = []
    for i in range(1, n + 1):
        row = []
        for j in range(i, i + n * (n - 1) + 1, n):
            row.append(j)
        matrix.append(row)
    return matrix


# Example usage
n = int(input("Enter a number: "))
result = generate_matrix(n)
for row in result:
    print(" ".join(map(str, row)))
