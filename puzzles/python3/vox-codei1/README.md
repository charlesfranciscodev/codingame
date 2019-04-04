# Vox Codei - Episode 1

The solution I used is a greedy solution. This means, on each turn we pick the bomb which will destroy the most nodes possible. This will work for all test cases except the last one. For the last test, we can simulate the entire game and see if all nodes have been destroyed with the available number of rounds and bombs. If the simulation fails, we pick a new location for the bomb until we suceed.
