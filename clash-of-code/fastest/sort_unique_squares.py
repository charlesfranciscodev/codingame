a = list(map(int, input().split(' ')))
b = set()
for x in a:
    b.add(x ** 2)
c = []
for y in b:
    c.append(y)
c.sort()
print(c)
