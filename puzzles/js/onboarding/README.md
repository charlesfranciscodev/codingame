Here's a possible solution to the "Onboarding" challenge on CodinGame using JavaScript:

```javascript
while (true) {
    const enemy1 = readline(); // name of enemy 1
    const dist1 = parseInt(readline()); // distance to enemy 1
    const enemy2 = readline(); // name of enemy 2
    const dist2 = parseInt(readline()); // distance to enemy 2

    // Determine which enemy is closer and print its name
    if (dist1 < dist2) {
        console.log(enemy1);
    } else {
        console.log(enemy2);
    }
}
```

In this solution, we use a `while` loop to continuously read input from the standard input until the program is terminated. In each iteration of the loop, we read the name and distance of two enemies, and then determine which one is closer based on their distances. Finally, we print the name of the closer enemy using `console.log()`.