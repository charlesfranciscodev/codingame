while True:
    highest_index = 0
    highest_height = -1

    # Read the heights of the mountains and determine the highest
    for i in range(8):
        mountain_height = int(input())
        
        # Check if this mountain is the highest so far
        if mountain_height > highest_height:
            highest_height = mountain_height
            highest_index = i

    # Output the index of the highest mountain to shoot
    print(highest_index)
