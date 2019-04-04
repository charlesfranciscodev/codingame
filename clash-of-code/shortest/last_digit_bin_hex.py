n=int(input())
x=hex(n)[-1]
if x.isalpha():
 x=ord(x)-87
print(bin(int(x))[-1])