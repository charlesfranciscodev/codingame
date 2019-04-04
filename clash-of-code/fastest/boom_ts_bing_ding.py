s = input()

x = 0
y = 0

for w in s.split():
    if w == "boom":
        if (x < 30):
            x += 1
    elif w == "ts":
        if (x > 0):
            x -= 1
    elif w == "bing":
        if (y < 10):
            y += 1
    elif w == "ding":
        if (y > 0):
            y -= 1

print("{} {}".format(x, y))
