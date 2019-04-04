s=input()
x=0
for c in s:
    x+=ord(c.lower())-ord('a')+1
print(x)