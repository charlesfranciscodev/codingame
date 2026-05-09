using System;
using System.Collections.Generic;

class Program
{
    static void Main(string[] args)
    {
        Dictionary<int, int> elevators = new Dictionary<int, int>();

        string[] inputLine = Console.ReadLine().Split();
        int exit_floor = int.Parse(inputLine[3]);
        int exit_pos = int.Parse(inputLine[4]);
        int n5 = int.Parse(inputLine[7]);

        for (int i = 0; i < n5; i++)
        {
            string[] elevatorLine = Console.ReadLine().Split();
            int elevator_floor = int.Parse(elevatorLine[0]);
            int elevator_pos = int.Parse(elevatorLine[1]);
            elevators[elevator_floor] = elevator_pos;
        }

        // For the last floor, we use the exit instead of an elevator.
        elevators[exit_floor] = exit_pos;

        // Game loop
        while (true)
        {
            string[] line = Console.ReadLine().Split();
            int clone_floor = int.Parse(line[0]);
            int clone_pos = int.Parse(line[1]);
            string direction = line[2];

            if (clone_floor == -1)
            {
                Console.WriteLine("WAIT");
            }
            else if (direction == "LEFT" && clone_pos < elevators[clone_floor])
            {
                Console.WriteLine("BLOCK");
            }
            else if (direction == "RIGHT" && clone_pos > elevators[clone_floor])
            {
                Console.WriteLine("BLOCK");
            }
            else
            {
                Console.WriteLine("WAIT");
            }
        }
    }
}
