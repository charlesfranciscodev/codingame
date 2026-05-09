s = set()
n = int(input())
for i in range(n):
    x = int(input())
    if x not in s:
        print(x)
        s.add(x)
