import math

s = int(input())  # s = x + y
p = int(input())  # p = x * y

# x**2 - x*s + p = 0
# a = 1, b = -s, c = p

delta = s ** 2 - 4 * p 

x1 = (s + math.sqrt(delta)) / 2
x2 = (s - math.sqrt(delta)) / 2

y1 = s - x1
y2 = s - x2

if x1 > y1:
    temp = x1
    x1 = y1
    y1 = temp

print("{} {}".format(round(x1), round(y1)))
