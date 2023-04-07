Sure, here's the same documentation without the conclusion section:

# The Descent

This is a Kotlin solution for the "The Descent" puzzle on [Codingame](https://www.codingame.com/ide/puzzle/the-descent).

## Problem Description

The goal of the puzzle is to destroy mountains, one by one, by shooting them with a cannon. You have a limited number of shots, and each shot destroys a single point on the mountain at the height of the shot. The objective is to destroy the highest mountain first and then move on to the next highest mountain, until all the mountains are destroyed.

The input for the puzzle is an array of integers representing the height of each mountain. The program should output the index of the highest mountain in the array, and then loop until all the mountains are destroyed.

## Solution

The solution uses a loop to keep firing shots until all the mountains are destroyed. At each iteration, the program finds the index of the highest mountain and fires a shot at that index. The program then updates the array to remove the destroyed point, and repeats the process until all the mountains are destroyed.

```kotlin
fun main() {
    // read in the mountain heights
    val mountainHeights = IntArray(8) { readLine()!!.toInt() }

    while (true) {
        // find the highest mountain
        val highestMountainIndex = mountainHeights.indexOf(mountainHeights.max())

        // fire a shot at the highest mountain
        println(highestMountainIndex)

        // update the mountain heights array
        mountainHeights[highestMountainIndex] = 0
    }
}
```

The program starts by reading in the mountain heights using the `readLine()` function. It then enters a loop that repeats until all the mountains have been destroyed. In each iteration of the loop, the program finds the index of the highest mountain using the `indexOf()` function, which returns the index of the first occurrence of the given element in the array. The program then fires a shot at the highest mountain by printing the index of the highest mountain to the console. Finally, the program updates the mountain heights array by setting the value of the highest mountain to 0.