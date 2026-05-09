def recamans_sequence(n):
    sequence = [0]  # Initialize the sequence with term 0

    for i in range(1, n):
        prev_term = sequence[i - 1]
        next_term = prev_term - i

        if next_term < 0 or next_term in sequence:
            next_term = prev_term + i

        sequence.append(next_term)

    return sequence


# Read the input value of n
n = int(input())

# Generate Recaman's sequence
result = recamans_sequence(n)

# Print the result
print(" ".join(map(str, result)))
