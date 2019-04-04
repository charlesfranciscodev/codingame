if __name__ == "__main__":
    """
    The while loop represents the game.
    Each iteration represents a turn of the game
    where you are given inputs (the heights of the mountains)
    and where you have to print an output (the index of the mountain to fire on).
    The inputs you are given are automatically updated according to your last actions.
    """
    while True:
        index_to_fire = 0
        max_mountain_height = -1
        for index in range(8):
            mountain_height = int(input())
            if mountain_height > max_mountain_height:
                max_mountain_height = mountain_height
                index_to_fire = index
        print(index_to_fire)
