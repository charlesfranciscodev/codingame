n = int(input())
s = 0
for i in input().split():
    x = int(i)
    s += x
res = s / n
print("{0:g}".format(res))
