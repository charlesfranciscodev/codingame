a = []
n = int(input())
for i in range(n):
    x = int(input())
    a.append(x)
a.sort()
a.reverse()
for i in range(len(a)):
    a[i] = str(a[i])
print(' '.join(a))