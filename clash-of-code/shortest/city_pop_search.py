n=int(input())
c=[]
for i in range(n):
 n,p=input().split()
 c.append((n,p))
s=input()
t=0
for n,p in c:
 if s in n:
  t+=int(p)
print(t)