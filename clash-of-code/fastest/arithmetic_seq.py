n, r = [int(i) for i in input().split()]
x = 0
a = []
for i in range(0, n):
    a.append(str(x))
    x += r
print(' '.join(a))
