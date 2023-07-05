MOD = 10**9


def compute_sums(n):
    sum_integers = (n * (n + 1) // 2) % MOD
    sum_squares = (n * (n + 1) * (2 * n + 1) // 6) % MOD
    sum_cubes = ((n * (n + 1) // 2) ** 2) % MOD

    return sum_integers, sum_squares, sum_cubes


if __name__ == "__main__":
    # Read input
    n = int(input())

    # Compute sums
    sum_integers, sum_squares, sum_cubes = compute_sums(n)

    # Print output
    print(sum_integers)
    print(sum_squares)
    print(sum_cubes)
