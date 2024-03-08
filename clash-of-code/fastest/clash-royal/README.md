# Clash Royal

This Python script simulates a Clash Royal match between two players, calculating the damage inflicted by one player on the other based on their level.

## `clash_royal_match(health, level)`
This function takes the health of the opposing player and the level of the attacker's card as input. It calculates the damage inflicted on the opposing player using the `calculate_damage` function and reduces the opposing player's health accordingly. If the opposing player's health reaches or falls below 0, the function returns a taunt message "hehehehaw" and the remaining health. Otherwise, it returns a victory message "rawr" and the remaining health.

## Usage
To use this script:
1. Run the script.
2. Input the health of the opposing player.
3. Input the level of your card.
4. The script will output the result of the match (taunt or victory message) and the remaining health of the opposing player.
