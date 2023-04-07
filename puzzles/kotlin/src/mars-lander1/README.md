# Mars Lander 1 Puzzle

This repository contains a Kotlin solution for the Mars Lander 1 puzzle on Codingame.

## Problem Statement

The Mars Lander 1 puzzle involves guiding a lander to a safe landing on the surface of Mars. The lander is subject to gravity and has a limited amount of fuel to control its descent. The goal is to land the lander at a specific landing zone without crashing or running out of fuel.

The puzzle consists of a series of test cases, each with its own landing zone and obstacles. The player must guide the lander through each test case, optimizing their fuel usage and trajectory to achieve a safe landing.

## Solution

The solution to the Mars Lander 1 puzzle is implemented in the `MarsLander1.kt` file. The solution uses a simple physics-based approach to simulate the lander's descent and control its trajectory.

The solution implements a loop that iterates over each time step of the simulation. At each time step, the solution calculates the lander's current state (position, velocity, fuel level) and determines the appropriate action to take (rotate the lander or fire the thrusters).

