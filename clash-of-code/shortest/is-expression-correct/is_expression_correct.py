def is_expression_correct(expression):
    stack = []

    for char in expression:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if len(stack) == 0 or stack[-1] != "(":
                return False
            stack.pop()

    return len(stack) == 0


# Testing the function
expression = input("Enter the expression: ")
print(is_expression_correct(expression))
