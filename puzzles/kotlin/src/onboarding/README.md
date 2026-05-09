This Kotlin code solves the "Onboarding" problem on CodinGame. The problem presents the player with two enemies and their respective distances, and the player must output the name of the enemy that is closer.

The code starts by importing the `Scanner` class from the `java.util` package. The `Scanner` class allows the program to read user input from the standard input stream.

The `main` function sets up an infinite loop that continuously reads input from the standard input stream. Within the loop, the program reads in the name of the first enemy and its distance using the `scanner.next()` and `scanner.nextInt()` methods, respectively. It then reads in the name of the second enemy and its distance in a similar way.

The program then compares the distances of the two enemies using an `if` statement. If the distance of the first enemy is less than the distance of the second enemy, the program outputs the name of the first enemy using the `println` method. Otherwise, it outputs the name of the second enemy.

The loop continues indefinitely, waiting for new input from the standard input stream.

```kotlin
import java.util.Scanner

fun main(args: Array<String>) {
    val scanner = Scanner(System.`in`)
    while (true) {
        val enemy1 = scanner.next() // name of enemy 1
        val dist1 = scanner.nextInt() // distance to enemy 1
        val enemy2 = scanner.next() // name of enemy 2
        val dist2 = scanner.nextInt() // distance to enemy 2

        if (dist1 < dist2) {
            println(enemy1)
        } else {
            println(enemy2)
        }
    }
}
```
