if __name__ == '__main__':
    while True:
        enemy_1 = input()  # name of enemy 1
        dist_1 = int(input())  # distance to enemy 1
        enemy_2 = input()  # name of enemy 2
        dist_2 = int(input())  # distance to enemy 2

        # Compare the distances of the two enemies
        if dist_1 < dist_2:
            # If enemy 1 is closer, shoot enemy 1
            print(enemy_1)
        else:
            # If enemy 2 is closer or at the same distance, shoot enemy 2
            print(enemy_2)
