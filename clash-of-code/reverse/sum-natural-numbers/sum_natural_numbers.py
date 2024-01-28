def find_output(input_number):
    return (input_number * (input_number + 1)) // 2


if __name__ == "__main__":
    n = int(input())
    output = find_output(n)
    print(output)
