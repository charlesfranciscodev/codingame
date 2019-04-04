n = int(input())
for i in range(1, n):
    if n % i == 0:
        print(i, end=' ')
print(n, end='')
