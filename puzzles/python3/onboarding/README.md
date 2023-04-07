Here's a possible solution to the "Onboarding" challenge on CodinGame using Python:

```python
while True:
    enemy_1 = input()  # name of enemy 1
    dist_1 = int(input())  # distance to enemy 1
    enemy_2 = input()  # name of enemy 2
    dist_2 = int(input())  # distance to enemy 2

    # Determine which enemy is closer and print its name
    if dist_1 < dist_2:
        print(enemy_1)
    else:
        print(enemy_2)
```

In this solution, we use a `while` loop to continuously read input from the standard input until the program is terminated. In each iteration of the loop, we read the name and distance of two enemies, and then determine which one is closer based on their distances. Finally, we print the name of the closer enemy using `print()`.
