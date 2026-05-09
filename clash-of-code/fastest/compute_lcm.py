from math import gcd

n = int(input())
a = []
for i in input().split():
    m = int(i)
    a.append(m)

lcm = a[0]
for i in a[1:]:
    lcm *= i // gcd(lcm, i)

print(lcm)
