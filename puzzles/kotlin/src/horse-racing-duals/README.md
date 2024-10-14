# Horse-racing Duals

## Problem Description

The goal of this puzzle is to find the two horses with the closest strength among a given number of horses. The strength of each horse is given as an integer. The program should output the difference between the strengths of the two closest horses.

### Inputs

Line 1: An integer N, the number of horses

The following N lines: The strength Pi of each horse, an integer

### Output

The difference D between the two closest strengths. D is an integer greater than or equal to 0.

### Constraints

1 < N < 100000
0 < Pi ≤ 10000000

### Example

#### Input
```
3
5
8
9
```

#### Output
```
1
```

## Code Example

```kotlin
import java.util.*

fun main(args: Array<String>) {
    val input = Scanner(System.`in`)
    val N = input.nextInt()
    
    // Read all the horse strengths into a list
    val strengths = mutableListOf<Int>()
    for (i in 0 until N) {
        strengths.add(input.nextInt())
    }

    // Sort the list of strengths
    strengths.sort()

    // Initialize a large minimum difference
    var minDifference = Int.MAX_VALUE

    // Compute the minimum difference between adjacent horses
    for (i in 0 until N - 1) {
        val diff = strengths[i + 1] - strengths[i]
        if (diff < minDifference) {
            minDifference = diff
        }
    }

    // Output the minimum difference
    println(minDifference)
}

```
