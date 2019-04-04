def strange(num):
    for x in range(0, num):
        y = x ** x + x
        if y == num:
            return True
        elif y > num:
            return False
    return False

num = int(input())
print(strange(num))

