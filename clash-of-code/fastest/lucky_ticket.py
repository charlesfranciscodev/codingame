n = int(input())
for i in range(n):
    t = input()
    first_sum = int(t[0]) + int(t[1]) + int(t[2])
    second_sum = int(t[3]) + int(t[4]) + int(t[5])
    if first_sum == second_sum:
        print("true")
    else:
        print("false")