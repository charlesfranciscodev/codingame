t = input()
t2 = input()
t3 = ""
for i in range(0, len(t)):
    x = int(t[i])
    y = int(t2[i])
    t3 += str(x | y)
    
print(t3)
