river_1 = int(input())
river_2 = int(input())

river_1_set = {river_1}
river_2_set = {river_2}

while True:
    river_1 += sum(map(int, str(river_1)))
    river_1_set.add(river_1)
    river_2 += sum(map(int, str(river_2)))
    river_2_set.add(river_2)
    if river_1 in river_2_set:
        print(river_1)
        break
    if river_2 in river_1_set:
        print(river_2)
        break
