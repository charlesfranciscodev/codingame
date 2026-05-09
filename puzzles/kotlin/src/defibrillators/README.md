# Defibrillators Puzzle

This is the solution for the Defibrillators puzzle from CodinGame, implemented in Kotlin.

The puzzle can be found at: [https://www.codingame.com/training/easy/defibrillators](https://www.codingame.com/training/easy/defibrillators)

## Problem Description

The goal of this puzzle is to find the closest defibrillator to a given location. The input contains a number of defibrillators, each with a name, a longitude, and a latitude. The user's location is also given as a longitude and latitude. The distance between two points can be calculated using the haversine formula.

## Solution Description

The solution reads in the user's location, the number of defibrillators, and the details of each defibrillator. For each defibrillator, the solution calculates the distance to the user's location using the haversine formula. The solution then keeps track of the closest defibrillator and returns its name.

## How to Run

The solution is implemented in Kotlin and can be run using the Kotlin compiler or an IDE such as IntelliJ IDEA. The code can be found in the `defibrillators.kt` file in the `src` folder.

The program can be run by providing the user's location and the details of the defibrillators as command line arguments. For example:

```
kotlin defibrillators.kt -3.879483,48.879678 3
"Defibrillator 1;6.145;49.986"
"Defibrillator 2;6.153;49.988"
"Defibrillator 3;6.155;49.990"
```