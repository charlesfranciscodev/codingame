s = input()
for c in s:
    if c.isupper():
        print(c.lower(), end='')
    else:
        print(c.upper(), end='')
