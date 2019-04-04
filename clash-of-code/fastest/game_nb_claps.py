n = int(input())

nb_claps = 0
for i in range(1, n + 1):
    s = str(i)
    if i % 7 == 0:
        nb_claps += 1
    elif '7' in s:
        nb_claps += 1
    elif sum(map(int, s)) % 7 == 0:
        nb_claps += 1

print(nb_claps)
