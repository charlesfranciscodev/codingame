if __name__ == "__main__":
    # game loop
    while True:
        enemy1: str = input()  # name of enemy 1
        distance1: int = int(input())  # distance to enemy 1
        enemy2: str = input()  # name of enemy 2
        distance2: int = int(input())  # distance to enemy 2

        # Display enemy1 name when enemy1 is the closest, enemy2 otherwise
        if distance1 < distance2:
            print(enemy1)
        else:
            print(enemy2)
