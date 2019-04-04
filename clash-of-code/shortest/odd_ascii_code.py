w=input()
s=0
for c in w:
 o=ord(c)
 if o%2:
  s+=o
print(s)