def find_lost_integer(numbers):
    counts = {}
    for num in numbers:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    for num, count in counts.items():
        if count % 2 != 0:
            return num

    return None


# Read input until 0 is encountered
numbers = []
while True:
    line = input().strip()
    if line == "0":
        break
    numbers.extend(map(int, line.split()))

lost_integer = find_lost_integer(numbers)
print(lost_integer)
