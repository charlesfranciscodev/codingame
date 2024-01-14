def can_return_to_first_element(N, A):
    visited = [False] * N
    current_index = 0

    while not visited[current_index]:
        # print(current_index, A[current_index])
        visited[current_index] = True
        current_index = A[current_index]

    return "returns" if current_index == 0 else "cycling"


if __name__ == "__main__":
    # Reading input
    N = int(input())
    A = [int(input()) for _ in range(N)]

    # Checking and printing the result
    result = can_return_to_first_element(N, A)
    print(result)
