# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

count = int(input())
out = 0
for i in input().split():
    n = int(i)
    if n % 2 == 0:
        out += n
    else:
        out *= n


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(out)
