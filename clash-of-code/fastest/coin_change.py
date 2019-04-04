s = input()
n = int(float(s[1:]) * 100.0)
coins = [100, 25, 10, 5, 1]
change = [0, 0, 0, 0, 0]

for i in range(0, len(coins)):
    while n - coins[i] >= 0:
        change[i] += 1
        n -= coins[i]

print(' '.join(map(str, change)))
