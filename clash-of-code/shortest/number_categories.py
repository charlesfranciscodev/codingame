from collections import defaultdict
c=defaultdict(set)
f=lambda:[int(i) for i in input().split()]
a,b=f()
s,e=f()
for i in range(s,e+1):
 x=i%a==0
 y=i%b==0
 if x and y:
  c[3].add(i)
 elif x and not y:
  c[1].add(i)
 elif y and not x:
  c[2].add(i)
 else:
  c[4].add(i)
o=[]
for i in range(1,5):
 o.append(str(len(c[i])))
print(' '.join(o))