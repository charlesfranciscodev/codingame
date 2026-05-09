

# temperatures.kt

This is a Kotlin solution for the "Temperatures" puzzle on the Codingame platform.

## Problem Description

Given a list of temperatures, find the temperature closest to zero. If two temperatures are equally close to zero, return the positive temperature.

### Input

- `n`: an integer, the number of temperatures in the list (0 ≤ `n` ≤ 1,000,000)
- `temperatures`: a space-separated list of `n` integers representing the temperatures (-273 ≤ `temperatures[i]` ≤ 5526)

### Output

- The temperature closest to zero. If two temperatures are equally close to zero, return the positive temperature.

## Solution Overview

To solve this problem, we need to find the temperature with the smallest absolute value that is greater than or equal to zero. We can do this by iterating over the list of temperatures and keeping track of the temperature with the smallest absolute value seen so far. If two temperatures have the same absolute value, we choose the positive one.

## Solution Details

Here's the code for the solution:

```kotlin
fun main(args : Array<String>) {
    val n = readLine()!!.toInt()
    val temperatures = readLine()!!.split(" ").map{ it.toInt() }

    var closestTemp = 5526 // The highest possible temperature
    for (temperature in temperatures) {
        val absTemp = kotlin.math.abs(temperature)
        val absClosestTemp = kotlin.math.abs(closestTemp)
        if (absTemp < absClosestTemp || (absTemp == absClosestTemp && temperature > 0)) {
            closestTemp = temperature
        }
    }

    println(closestTemp)
}
```

Here's how the solution works:

1. We read in the input values of `n` and `temperatures` using `readLine()!!`.
2. We set `closestTemp` to the highest possible temperature, `5526`.
3. We iterate over the list of temperatures using a for loop, and for each temperature:
   - We calculate its absolute value using `kotlin.math.abs(temperature)`.
   - We calculate the absolute value of `closestTemp` using `kotlin.math.abs(closestTemp)`.
   - If the absolute value of the current temperature is smaller than the absolute value of `closestTemp`, or if the absolute values are equal and the current temperature is positive, we update `closestTemp` to the current temperature.
4. We print the final value of `closestTemp`.

## Conclusion

This Kotlin solution uses a simple algorithm to find the temperature closest to zero in a given list of temperatures. By keeping track of the temperature with the smallest absolute value seen so far, we can efficiently find the desired temperature.