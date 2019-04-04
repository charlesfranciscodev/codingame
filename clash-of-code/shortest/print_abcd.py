a=int(input())
b=int(input())
c=int(input())
d=int(input())
for _ in range(d):
 e = []
 for _ in range(c):
  e.append(str(a))
  a += b
 print(' '.join(e))