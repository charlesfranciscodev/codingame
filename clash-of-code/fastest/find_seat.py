# Read Bob's seat and Erica's seat coordinates
rb, cb = map(int, input().split())
re, ce = map(int, input().split())

# Calculate the midpoint coordinates
rj = (rb + re) // 2
cj = (cb + ce) // 2

# Output Jack's seat coordinates
print(rj, cj)
