using System;
using System.Collections.Generic;

class Program
{
    static void Main(string[] args)
    {
        const char EMPTY = '.';
        const char NODE = '0';
        List<string> grid = new List<string>();

        int width = int.Parse(Console.ReadLine()); // the number of cells on the X axis
        int height = int.Parse(Console.ReadLine()); // the number of cells on the Y axis
        for (int i = 0; i < height; i++)
        {
            grid.Add(Console.ReadLine());
        }

        for (int y = 0; y < height; y++)
        {
            for (int x = 0; x < width; x++)
            {
                if (grid[y][x] == NODE)
                {
                    // node
                    string output = $"{x} {y} ";

                    // right neighbor
                    char neighbor = EMPTY;
                    for (int neighbor_x = x + 1; neighbor_x < width; neighbor_x++)
                    {
                        neighbor = grid[y][neighbor_x];
                        if (neighbor == NODE)
                        {
                            output += $"{neighbor_x} {y} ";
                            break;
                        }
                    }

                    if (neighbor == EMPTY)
                    {
                        output += "-1 -1 ";
                    }

                    // bottom neighbor
                    neighbor = EMPTY;
                    for (int neighbor_y = y + 1; neighbor_y < height; neighbor_y++)
                    {
                        neighbor = grid[neighbor_y][x];
                        if (neighbor == NODE)
                        {
                            output += $"{x} {neighbor_y} ";
                            break;
                        }
                    }

                    if (neighbor == EMPTY)
                    {
                        output += "-1 -1 ";
                    }

                    Console.WriteLine(output);
                }
            }
        }
    }
}
