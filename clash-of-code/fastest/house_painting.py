paint = int(input())
nb_rooms = int(input())
total_surface = 0
for i in range(nb_rooms):
    x, y, z = map(int, input().split())
    surface = x * y + y * z + x * z
    total_surface += surface
if total_surface <= (paint * 5):
    print("true")
else:
    print("false")
