# Blunder - Episode 1

In this puzzle, you will learn about parsing, storing, and manipulating two-dimensional arrays. These arrays serve as the basis for solving 2D problems. Additionally, you will implement a simple but complete Finite State Machine and gain an understanding of this concept.

To solve the puzzle, you will assist Blunder, a robot, in navigating through a city. Your task is to determine the robot's next movement based on its previous moves and the environment, including obstacles. It is essential to carefully read and understand the rules for the robot's displacement and how to represent the city's map.

This puzzle presents learning opportunities in the following concepts:

1. State machine: You will implement a Finite State Machine, a computational model that consists of a set of states and transitions between them. It allows you to represent and control the behavior of the robot based on its current state and inputs.

2. Simulation: You will simulate the movement of the robot through the city by manipulating the two-dimensional arrays. This involves updating the robot's position and checking for obstacles or other conditions that affect its movement.

By solving this puzzle, you will enhance your skills in state machine design and simulation techniques using two-dimensional arrays.

We have to print Blunder's path in the maze and also be able to detect infinite loops.
We can detect loops by checking if Blunder passed a cell twice in the same state and with no modifications to the map in between.
