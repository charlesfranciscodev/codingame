using System;
using System.Collections.Generic;

public class Program
{
    public static void Main(string[] args)
    {
        List<List<int>> rooms = new List<List<int>>();
        string[] inputParams = Console.ReadLine().Split();
        int nbColumns = int.Parse(inputParams[0]);
        int nbRows = int.Parse(inputParams[1]);
        for (int i = 0; i < nbRows; i++)
        {
            rooms.Add(new List<int>(Array.ConvertAll(Console.ReadLine().Split(), int.Parse)));
        }
        int ex = int.Parse(Console.ReadLine());

        // game loop
        while (true)
        {
            string[] line = Console.ReadLine().Split();
            int x = int.Parse(line[0]);
            int y = int.Parse(line[1]);
            string entrance = line[2];
            PrintNextRoom(rooms[y][x], ref x, ref y, entrance);
        }
    }

    public static void PrintNextRoom(int roomType, ref int x, ref int y, string entrance)
    {
        if (roomType == 2 || roomType == 6)
        {
            if (entrance == "LEFT")
            {
                x += 1;
            }
            else
            {
                x -= 1;
            }
        }
        else if (roomType == 4)
        {
            if (entrance == "TOP")
            {
                x -= 1;
            }
            else
            {
                y += 1;
            }
        }
        else if (roomType == 5)
        {
            if (entrance == "TOP")
            {
                x += 1;
            }
            else
            {
                y += 1;
            }
        }
        else if (roomType == 10)
        {
            x -= 1;
        }
        else if (roomType == 11)
        {
            x += 1;
        }
        else
        {
            y += 1;
        }
        Console.WriteLine($"{x} {y}");
    }
}
