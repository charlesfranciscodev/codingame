if __name__ == "__main__":
    n = int(input())
    levels = [int(i) for i in input().split()]

    update = True
    while update:
        update = False
        visited = set()
        for level in levels:
            if level not in visited:
                visited.add(level)
            else:
                update = True
                levels.append(level + 1)  # combine the 2 stones
                levels.remove(level)
                levels.remove(level)
                visited.remove(level)

    print(len(levels))
