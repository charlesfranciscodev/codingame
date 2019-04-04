c={}
for i in range(int(input())):
 n=input()
 c[n.replace(' ', '').lower()]=n
for i in range(int(input())):
 print(c[input().replace(' ', '').lower()])