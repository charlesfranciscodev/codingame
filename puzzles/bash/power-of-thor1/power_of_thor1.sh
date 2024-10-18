# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print thorX and thorY if Thor seems not to follow your orders.

# lightX: the X position of the light of power
# lightY: the Y position of the light of power
# thorX: Thor's current X position
# thorY: Thor's current Y position
read -r lightX lightY thorX thorY

# game loop
while true; do
    # remainingTurns: The remaining amount of turns Thor can move. Do not remove this line.
    read -r remainingTurns

    # Calculate the direction
    direction=""

    # Determine the vertical direction (N or S) and update position
    if [ "$thorY" -gt "$lightY" ]; then
        direction+="N"
        ((thorY--))
    elif [ "$thorY" -lt "$lightY" ]; then
        direction+="S"
        ((thorY++))
    fi

    # Determine the horizontal direction (E or W) and update position
    if [ "$thorX" -gt "$lightX" ]; then
        direction+="W"
        ((thorX--))
    elif [ "$thorX" -lt "$lightX" ]; then
        direction+="E"
        ((thorX++))
    fi

    # Output the direction
    echo "$direction"
done
