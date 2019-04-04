if __name__ == "__main__":
    light_x, light_y, thor_x, thor_y = map(int, input().split())

    # game loop
    while True:
        direction = ""

        if thor_y > light_y:
            direction += "N"
            thor_y -= 1
        elif thor_y < light_y:
            direction += "S"
            thor_y += 1

        if thor_x > light_x:
            direction += "W"
            thor_x -= 1
        elif thor_x < light_x:
            direction += "E"
            thor_x += 1

        # A single line providing the move to be made: N NE E SE S SW W or NW
        print(direction)
