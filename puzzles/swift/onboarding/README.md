Documentation for the onboarding.swift file in the codingame repository is as follows:

## Description
This file contains the solution to the "Onboarding" puzzle on the Codingame platform, implemented in the Swift programming language. The puzzle requires the program to read the names of enemy spaceships and their distances from the player's spaceship, and then output the name of the closest enemy spaceship.

## Functionality
The program contains a single function `main()`, which is the entry point for the program. It takes no arguments and returns no values. Within the `main()` function, the program reads input from the standard input using the `readLine()` function, and then uses string manipulation and conditional statements to determine the name of the closest enemy spaceship. Finally, the program outputs the name of the closest enemy using the `print()` function.

## Input
The input for this puzzle consists of a series of lines, each containing the name of an enemy spaceship and its distance from the player's spaceship. The input is terminated by a line containing the word "END". The input format for each line is as follows:

```
{enemy_name} {distance}
```

Where `{enemy_name}` is a string containing the name of the enemy spaceship, and `{distance}` is an integer representing the distance of the enemy spaceship from the player's spaceship.

## Output
The output for this puzzle consists of a single line containing the name of the closest enemy spaceship. The output format is as follows:

```
{enemy_name}
```

Where `{enemy_name}` is the name of the closest enemy spaceship.

## Example
Input:
```
Buzz 9999
Bob 10000
END
```

Output:
```
Buzz
```

In this example, the enemy spaceship named "Buzz" is the closest to the player's spaceship, since it is only 9999 units away, whereas the enemy spaceship named "Bob" is 10000 units away. Therefore, the program outputs "Buzz".

## Example Solution

```swift
while true {
    let enemy1 = readLine()! // name of enemy 1
    let dist1 = Int(readLine()!)! // distance to enemy 1
    let enemy2 = readLine()! // name of enemy 2
    let dist2 = Int(readLine()!)! // distance to enemy 2
    
    if dist1 < dist2 {
        print(enemy1)
    } else {
        print(enemy2)
    }
}
```

The above code uses a `while true` loop to continuously read input from standard input (which is provided by CodinGame) and print the name of the closest enemy.

In each iteration of the loop, we first read in the name and distance of the first enemy, and store them in the `enemy1` and `dist1` variables. We do the same for the second enemy, storing their name and distance in the `enemy2` and `dist2` variables.

We then compare the distances of the two enemies, and print the name of the one that is closest. Note that the `readLine()` function returns an optional string, so we use the `!` operator to force unwrap the optionals and convert the distance to an `Int`.
