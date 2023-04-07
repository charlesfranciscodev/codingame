# Horse Racing Duals

This is a solution to the Horse Racing Duals puzzle on [CodinGame](https://www.codingame.com/ide/puzzle/horse-racing-duals).

## Problem Description

Given `N` integers representing the strengths of `N` horses, your goal is to find the minimum absolute difference between the strengths of any two horses in a pair. You must output this minimum difference.

## Solution

The approach to solve this problem is to sort the list of horse strengths in ascending order and then compute the absolute difference between adjacent horses. The smallest difference found is the minimum absolute difference between the strengths of any two horses.

## Code Explanation

The code begins with reading the integer `N` from the input. This is followed by reading `N` integers representing the strengths of the `N` horses. These strengths are stored in a list.

The list of horse strengths is then sorted in ascending order using the `sorted()` function. A new list is created by computing the absolute difference between adjacent strengths in the sorted list. The minimum absolute difference found in this new list is the minimum absolute difference between the strengths of any two horses.

Finally, the minimum absolute difference is printed to the console.

```kotlin
import java.util.*

fun main(args : Array<String>) {

    val input = Scanner(System.`in`)
    val n = input.nextInt()

    val strengths = mutableListOf<Int>()
    for (i in 0 until n) {
        strengths.add(input.nextInt())
    }

    strengths.sort()
    val differences = mutableListOf<Int>()
    for (i in 0 until n-1) {
        differences.add(strengths[i+1] - strengths[i])
    }

    println(differences.min())
}
```

## Conclusion

This solution shows that sorting a list and then computing differences between adjacent elements is an effective way to solve this problem. The code is concise and easy to understand.