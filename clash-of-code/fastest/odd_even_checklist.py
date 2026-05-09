def print_checklist(count, numbers):
    checklist = []
    for num in numbers:
        if num % 2 == 0:
            checklist.append(f"[ ] {num}")
        else:
            checklist.append(f"[x] {num}")
    return checklist


# Test Case 1
input1 = (5, [1, 2, 3, 4, 5])
output1 = ["[x] 1", "[ ] 2", "[x] 3", "[ ] 4", "[x] 5"]
assert print_checklist(*input1) == output1

# Test Case 2
input2 = (3, [10, -5, 8])
output2 = ["[ ] 10", "[x] -5", "[ ] 8"]
assert print_checklist(*input2) == output2

# Test Case 3
input3 = (6, [0, 21, -12, 7, 4, -3])
output3 = ["[ ] 0", "[x] 21", "[ ] -12", "[x] 7", "[ ] 4", "[x] -3"]
assert print_checklist(*input3) == output3

# Add more test cases as needed

print("All test cases passed!")
