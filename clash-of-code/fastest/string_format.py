s = input()
f = input()
i = 0
j = 0
while i < len(f):
    c = f[i]
    if c == 'x':
        print(s[j].lower(), end='')
        i += 1
        j += 1
    elif c == 'X':
        print(s[j].upper(), end='')
        i += 1
        j += 1
    else:
        print(f[i], end='')
        i += 1

