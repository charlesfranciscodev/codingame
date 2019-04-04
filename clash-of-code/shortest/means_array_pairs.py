n = int(input())
y = list(map(int, input().split()))
i = 0
while i < n - 2:
    c = (y[i] + y[i + 1]) / 2
    print("{0:g}".format(c), end=' ')
    i += 2
a = y[i]
b = 0
if (i < n - 1):
    b = y[i + 1]
print("{0:g}".format((a + b) / 2), end='')
