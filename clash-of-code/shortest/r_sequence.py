n=int(input())
d=set()
r=[0]
for i in range(1,n+1):
 x=r[i-1]-i
 if x>0 and x not in d:
  d.add(x)
  r.append(x)
 else:
  x=r[i-1]+i
  d.add(x)
  r.append(x)
print(r[-1])
