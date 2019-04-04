a=[]
n=int(input())
for i in input().split():
 a.append(int(i))
a.sort()
for j in range(len(a)):
 a[j] = str(a[j])
print(' '.join(a))