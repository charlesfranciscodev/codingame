# Power of Thor

This is a solution to the Power of Thor puzzle on [Codingame](https://www.codingame.com/training/easy/power-of-thor-episode-1) implemented in Swift.

## Problem Description

In this puzzle, Thor is stranded on a rectangular grid and needs to reach a lightning bolt that is located at a specific position on the grid. The position of Thor and the lightning bolt are given as input to the program. Thor can move in four directions: North, South, East, and West. For each move, the program needs to output the direction in which Thor should move to get closer to the lightning bolt.

## Solution Overview

The solution uses a loop to iterate over the possible moves of Thor. At each iteration, the program calculates the direction in which Thor should move based on his current position and the position of the lightning bolt. The program then outputs the direction in which Thor should move and updates his position accordingly.

## Code Explanation

The code starts by reading the input values from standard input using the `readLine()` function. The input values are then parsed into variables.

```swift
let inputs = (readLine()!).split(separator: " ").map(String.init)
let lightX = Int(inputs[0])!
let lightY = Int(inputs[1])!
let initialTx = Int(inputs[2])!
let initialTy = Int(inputs[3])!
```

The program then enters a loop that runs until Thor reaches the lightning bolt. At each iteration of the loop, the program calculates the direction in which Thor should move based on his current position and the position of the lightning bolt.

```swift
while true {
    let remainingTurns = Int(readLine()!)!
    var direction = ""

    if initialTy > lightY {
        direction += "N"
        initialTy -= 1
    } else if initialTy < lightY {
        direction += "S"
        initialTy += 1
    }

    if initialTx > lightX {
        direction += "W"
        initialTx -= 1
    } else if initialTx < lightX {
        direction += "E"
        initialTx += 1
    }

    print(direction)
}
```

The loop also reads in the remaining turns from standard input and assigns it to the `remainingTurns` variable. Finally, the program outputs the direction in which Thor should move and updates his position.

## Conclusion

This solution demonstrates how to solve the Power of Thor puzzle on Codingame using Swift. The program reads in input values from standard input, enters a loop to calculate the direction in which Thor should move, and outputs the direction in which he should move. This solution can be used as a starting point to solve other puzzles on Codingame or similar platforms.
