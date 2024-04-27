# Vox Codei - Episode 1

## Problem Description

VoxCodei is a game where the player controls a character tasked with destroying targets within a grid-based environment. The grid contains walls, empty spaces, and targets represented by symbols. The player has limited rounds and a set number of bombs to accomplish the task. Each bomb placed has a range within which it can destroy targets. The goal is to strategically place bombs to maximize the destruction of targets within the given constraints.

## Solution Overview

The game environment is represented by a grid, where each cell contains information about its contents, including whether it's a target, a wall, empty space, or a destructible target. The character can place bombs strategically to destroy targets within their blast radius.

1. **Grid Representation:** The game environment is represented by a 2D grid, where each cell is a Node object containing information about its state.

2. **Bomb Placement:** The character can place bombs on empty spaces or destructible targets. When a bomb is placed, it triggers an explosion that destroys targets within its blast radius.

3. **Scoring:** The score is calculated based on the number of targets destroyed by each bomb placement. A higher score indicates a more effective bomb placement strategy.

4. **Game Loop:** The game proceeds in rounds, where the character must decide where to place bombs within the given constraints. The game loop continues until all targets are destroyed or the rounds run out.

5. **Simulation:** To determine the effectiveness of a bomb placement, a simulation is performed to predict the outcome of the explosion. This simulation considers the blast radius of the bomb and updates the grid accordingly.

6. **Strategy:** The character employs a greedy strategy to maximize the destruction of targets. It evaluates potential bomb placements based on the resulting score and selects the one with the highest score.

7. **Validation:** Bomb placements are validated to ensure they are within the grid boundaries and on valid positions.

8. **Game Termination:** The game terminates when either all targets are destroyed or the rounds run out.
