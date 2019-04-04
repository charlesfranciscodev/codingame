import sys

size = int(input())
half_length = size * 2 - 2

for i in range(1, size + 1):
    for j in range(0, i + 1):
        spaces = half_length - j
        middle = (j + 1) * 2 - 1
        for i in range(0, spaces):
            print(" ", end='')
        for i in range(0, middle):
            print("*", end='')
        print(" ")

# base of the tree
for i in range(0, half_length):
    print(" ", end='')
print("| ")

for i in range(0, half_length):
    print("=", end='')
print("V", end='')
for i in range(0, half_length):
    print("=", end='')
