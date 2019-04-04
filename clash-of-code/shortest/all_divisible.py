n=int(input())
m=int(input())
p=list(map(int,input().split()))
for i in input().split():
 x=int(i)
 d=all(x%y==0 for y in p)
 c='T' if d else 'F'
 print(c,end='')