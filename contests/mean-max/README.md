# MEAN MAX

## Overview:
MEAN MAX is a strategy game where the objective is to gather more water than your opponents. Players control Reapers, tasked with harvesting water from the wrecks of tankers on a circular map. The game ends when any player reaches 50 water or after 200 turns.

## Game Mechanics:
- **Map**: The game is played on a circular area with a radius of 6000.
- **Players**: There are three players, each starting with a Reaper.
- **Reapers**: Reapers harvest 1 water per turn from each wreck they occupy.
- **Actions**: Players can either move their Reaper towards a specific position or choose to wait.
- **Ending Conditions**: The game ends when any player reaches 50 water or after 200 turns.

## Rules:
- **Movement**: Reapers can accelerate towards a specific point on the map.
- **Harvesting**: Reapers collect water from wrecks by being in their vicinity at the end of a turn.
- **Collisions**: Collisions between units are inelastic.
- **Friction**: Friction is applied at the end of each turn.
- **Scoring**: Players earn water by harvesting wrecks.

## Input and Output Format:
- **Input**: Each game turn includes information about player scores, unit positions, and velocities.
- **Output**: Players must specify the direction and throttle for their Reaper's acceleration or choose to wait.

## Technical Details:
- **Reaper Attributes**: Mass = 0.5, Friction = 0.2
- **Unit Types**: Reapers (Type 0) and Wrecks (Type 4)
- **Unit Data**: Includes ID, Type, Player ID, Mass, Radius, Position, Velocity, and Water Quantity (for wrecks).

## Sample Input Format (One Game Turn):
- First 3 lines: Scores of each player
- Next 3 lines: Placeholder for future leagues
- Line 10: Number of units
- Following lines: Unit data (ID, Type, Player ID, Mass, Radius, Position, Velocity, Water Quantity)

## Sample Output Format (One Game Turn):
- One line for player's Reaper: Direction (X, Y) and Throttle
- Two lines of WAIT (for future leagues)

## Notes:
- Players need to strategize movement to maximize water collection while avoiding collisions.
- Precision in acceleration and positioning is crucial for efficient resource gathering.
- Friction affects velocity, influencing movement decisions.

Enjoy playing MEAN MAX!
