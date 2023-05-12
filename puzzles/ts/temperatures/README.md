# Temperatures

## Description

"Temperatures" is a beginner-level coding challenge available on the CodinGame platform. In this challenge, the player is given a list of integers representing temperature readings in Celsius degrees for a city during a certain period of time.

The objective is to write a program that finds and outputs the closest temperature to zero. If there are two temperatures that are equally close to zero, the program should output the positive one.

The challenge consists of writing a program that takes as input the list of temperature readings and outputs the temperature closest to zero. If the list is empty, the program should output 0.

The challenge is designed to help players learn and practice programming skills such as array manipulation, looping, and conditional statements. It is a fun and engaging way to improve programming skills while solving a challenging and entertaining puzzle.

## Solution

```typescript
function closestToZero(temperatures: number[]): number {
    let closest = Infinity;
  
    for (let i = 0; i < temperatures.length; i++) {
      if (Math.abs(temperatures[i]) < Math.abs(closest)) {
        closest = temperatures[i];
      } else if (Math.abs(temperatures[i]) === Math.abs(closest) && temperatures[i] > closest) {
        closest = temperatures[i];
      }
    }
  
    return closest;
}
  
// Reading input from standard input
const numTemperatures: number = parseInt(readline()); // the number of temperatures to analyse
var inputs: number[] = readline().split(" ").map(Number);
const result = closestToZero(inputs);
console.log(result);
```
