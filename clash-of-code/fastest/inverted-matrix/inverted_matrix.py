# Read input values
a, b = map(float, input().split())
c, d = map(float, input().split())

# Calculate determinant
det = a * d - b * c

# Check if determinant is non-zero
if det == 0:
    print("IMPOSSIBLE")
else:
    # Calculate inverse matrix elements
    inv_a = d / det
    inv_b = -b / det
    inv_c = -c / det
    inv_d = a / det

    # Print inverted matrix elements with 3 decimal places
    print(f"{inv_a:.3f} {inv_b:.3f}")
    print(f"{inv_c:.3f} {inv_d:.3f}")
