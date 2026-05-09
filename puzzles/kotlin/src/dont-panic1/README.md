

# Dont-Panic1 Puzzle Solution

This is a markdown documentation for the Kotlin solution of the Dont-Panic1 puzzle on CodinGame. The solution can be found in the following file:

- https://github.com/charlesfranciscodev/codingame/blob/master/puzzles/kotlin/src/dont-panic1.kt

## Problem Description

The puzzle is about a worker in a building where the floors are numbered from 0 (ground floor) to N. The worker is trying to reach a certain floor F, but the elevator he is in only stops on certain floors.

The worker is given a set of instructions to follow in order to reach his desired floor. The instructions are in the form of pairs (floor, direction), where `floor` is the floor number that the worker must get off on, and `direction` is either "LEFT" or "RIGHT", indicating the direction the worker must walk from the elevator.

If the worker reaches the desired floor F, the puzzle is solved. Otherwise, the worker must follow the instructions until he reaches the desired floor or falls off the building.

## Solution Overview

The solution to this puzzle involves simulating the movement of the worker in the building. We start by reading in the input data and parsing it into a more convenient format.

Next, we initialize the state of the worker by setting his current floor and direction. We then iterate through the instructions, simulating the worker's movement on each floor.

On each floor, we check if the worker needs to get off on that floor. If so, we check if he is going in the correct direction. If not, we change his direction and add an additional turn to his total turn count.

Finally, we output the total turn count, which represents the minimum number of turns required for the worker to reach his desired floor.

## Parsing the Input

The input for this puzzle is given in the following format:

```
N P F
elevators
num_of_instructions
instruction_1
instruction_2
...
instruction_N
```

- `N` is the number of floors in the building.
- `P` is the position of the elevator on the starting floor.
- `F` is the desired floor that the worker wants to reach.
- `elevators` is a string of length N indicating which floors have elevators. A character of `0` means there is no elevator on that floor, and a character of `1` means there is an elevator.
- `num_of_instructions` is the number of instructions that the worker must follow.
- `instruction_i` is a pair of integers and a string representing the floor number, the direction (LEFT or RIGHT), and a space-separated pair of integers representing the floor number and the direction (LEFT or RIGHT).

We start by reading in the first line of input and parsing `N`, `P`, and `F`:

```kotlin
val (numFloors, elevatorPos, targetFloor) = readLine()!!.split(" ").map { it.toInt() }
```

Next, we read in the string `elevators` and convert it to a list of booleans using the `map` function:

```kotlin
val elevators = readLine()!!.map { it == '1' }
```

We then read in the number of instructions and parse each instruction into a pair of integers and a string:

```kotlin
val numInstructions = readLine()!!.toInt()
val instructions = List(numInstructions) {
    val (floor, direction) = readLine()!!.split(" ")
    val (floorNum, directionStr) = direction.split("-")
    floorNum.toInt() to directionStr
}
```
