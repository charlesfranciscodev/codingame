t, h, w = input().split()
t = float(t)
h = int(h)
w = int(w)

nb_folds = 0
start_width = w
while t < h:
    t *= 2
    w *= 2
    nb_folds += 1

print(nb_folds)
print(w)
