a = []
n = int(input())
for i in range(n):
    line = input().split(',')
    a.append((line[0], int(line[1])))

swapped = True
nb_pages = 0
while swapped:
    swapped = False
    for i in range(0, len(a) - 1):
        if a[i][0] > a[i + 1][0]:
            nb_pages += (a[i][1] + a[i + 1][1])
            temp = a[i]
            a[i] = a[i + 1]
            a[i + 1] = temp
            swapped = True

print(nb_pages)
