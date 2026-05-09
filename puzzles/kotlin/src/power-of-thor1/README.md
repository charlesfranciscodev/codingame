# Power of Thor Puzzle Solution in Kotlin

## Problem Description

In the Power of Thor puzzle on [CodinGame](https://www.codingame.com/training/easy/power-of-thor-episode-1), you control Thor, who has to reach the light of power located at a certain (x, y) coordinate. Thor starts at a different (x, y) coordinate on the map and has a limited amount of energy.

On each turn, you must print the direction in which Thor should move towards the light of power: North, South, East, or West.

## Code Explanation

The solution is implemented in the `main` function of the `PowerOfThor1.kt` file. The main function reads the initial values of Thor's position (`x` and `y`) and the position of the light of power (`lightX` and `lightY`) from the standard input.

The function then enters a loop that runs until Thor reaches the light of power. In each iteration of the loop, the function calculates the direction in which Thor should move by comparing Thor's current position to the position of the light of power.

The direction is printed to the console, and Thor's position is updated accordingly. The loop continues until Thor reaches the light of power.