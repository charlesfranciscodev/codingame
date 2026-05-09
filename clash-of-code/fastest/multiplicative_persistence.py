n = int(input())
nb_steps = 0
while len(str(n)) != 1:
    m = 1
    for c in str(n):
        m *= int(c)
    n = m
    nb_steps += 1
print(nb_steps)
