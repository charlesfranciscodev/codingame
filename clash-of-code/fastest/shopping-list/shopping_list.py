def calculate_shopping_cost():
    # Read the number of items on the shopping list
    N = int(input())

    # Create a dictionary to store the items and their quantities
    shopping_list = {}

    # Read the items on the shopping list
    for _ in range(N):
        item = input()
        if item in shopping_list:
            shopping_list[item] += 1
        else:
            shopping_list[item] = 1

    # Read the number of items in the store
    C = int(input())

    # Initialize the total cost
    total_cost = 0

    # Read the items available in the store and calculate the total cost
    for _ in range(C):
        item, cost = input().split()
        if item in shopping_list:
            quantity = shopping_list[item]
            total_cost += int(cost) * quantity

    # Print the total cost
    print(total_cost)


# Call the function to calculate the shopping cost
calculate_shopping_cost()
