# Read input values
a = int(input())
b = int(input())
c = int(input())

# Calculate the total earnings in four weeks
earnings = a * 6 * 5 * 4

# Calculate the total expenses in four weeks
expenses = b + c

# Check if he can afford the apartment
if earnings >= expenses:
    print("true")
else:
    print("false")
