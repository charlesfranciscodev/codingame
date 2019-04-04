def f(c, t):
 d={'u':'A','l':'a','d':'0'}
 s=d[t]
 for i in range(0,ord(c)-ord(s)+1):
  print(chr(ord(s)+i),end='')
s=input()
for c in s:
 if c.isupper():
  f(c,'u')
 elif c.islower():
  f(c,'l')
 elif c.isdigit():
  f(c,'d')