def f(s):
 e=[]
 a=''
 x=0
 for c in s:
  if (c == a):
   x += 1
  else:
   if (x!=0):
    e.append(str(x))
    e.append(a)
   a=c
   x=1
 e.append(str(x))
 e.append(a)
 return ''.join(e)
s = input()
print(f(s))