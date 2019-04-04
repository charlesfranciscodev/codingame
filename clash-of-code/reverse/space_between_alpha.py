s = input()
i = 0
while i < len(s):
    c1 = s[i]
    if i == len(s) - 1:
        print(c1, end='')
        i += 1
        continue
    c2 = s[i + 1]
    if c1.isalpha() and c2.isalpha():
        print(c1 + ' ', end='')
    else:
        print(c1, end='')
    i += 1
