score = 0
pars = []
for i in input().split():
    x = int(i)
    pars.append(x)
for index, i in enumerate(input().split()):
    x = int(i)
    par = pars[index]
    score += x - par
print(score)
