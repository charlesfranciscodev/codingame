# Roller Coaster

The goal of this puzzle is to simulate the ride of a queue of people on a rollercoaster. The queue forms a cycle so there is something to exploit there in order to speed up your simulation.

This is possible with dynamic programming. The idea is to calculate the earnings starting from each group (1 ride) and to save the result in an array. Then we can calculate the total earnings starting from the first group (for all rides).
