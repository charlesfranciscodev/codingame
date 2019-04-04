x=0
a=input().split()
for s in a:
 if s=="inc":
  x+=1
 elif s=="dec":
  x-=1
 elif s=="print":
  print(x, end='')
 elif s=="double":
  x*=2
 elif s=="half":
  x//= 2
 else:
  break
