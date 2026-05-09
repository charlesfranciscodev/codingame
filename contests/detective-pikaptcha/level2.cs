using System;
using System.Collections.Generic;

public class Pikachu
{
    public (int, int) start = (0, 0);
    public (int, int) previous = (0, 0);
    public int x = 0;
    public int y = 0;
    public string facing = "";
    public Dictionary<string, List<string>> priorities = new Dictionary<string, List<string>>();

    public bool IsTrapped()
    {
        return previous == (x, y);
    }
}

public class Game
{
    private const char WALL = '#';

    private const string FOLLOW_RIGHT = "R";
    private const string FOLLOW_LEFT = "L";

    private const string RIGHT = ">";
    private const string DOWN = "v";
    private const string LEFT = "<";
    private const string UP = "^";

    private readonly string[] DIRECTIONS = { RIGHT, DOWN, LEFT, UP };

    private List<string[]> rows = new List<string[]>();
    private int width = 0;
    private int height = 0;
    private Pikachu pika = new Pikachu();

    public void ReadInput()
    {
        string[] dimensions = Console.ReadLine().Split();
        width = int.Parse(dimensions[0]);
        height = int.Parse(dimensions[1]);

        for (int y = 0; y < height; y++)
        {
            string line = Console.ReadLine();
            rows.Add(new string[width]);
            for (int x = 0; x < width; x++)
            {
                if (Array.IndexOf(DIRECTIONS, line[x].ToString()) != -1)
                {
                    pika.start = (x, y);
                    pika.x = x;
                    pika.y = y;
                    pika.facing = line[x].ToString();
                }
                if (line[x] == WALL)
                {
                    rows[y][x] = WALL.ToString();
                }
                else
                {
                    rows[y][x] = "0";
                }
            }
        }

        string follow = Console.ReadLine();
        if (follow == FOLLOW_RIGHT)
        {
            pika.priorities = new Dictionary<string, List<string>>()
            {
                { UP, new List<string> { RIGHT, UP, LEFT, DOWN } },
                { DOWN, new List<string> { LEFT, DOWN, RIGHT, UP } },
                { RIGHT, new List<string> { DOWN, RIGHT, UP, LEFT } },
                { LEFT, new List<string> { UP, LEFT, DOWN, RIGHT } }
            };
        }
        else if (follow == FOLLOW_LEFT)
        {
            pika.priorities = new Dictionary<string, List<string>>()
            {
                { UP, new List<string> { LEFT, UP, RIGHT, DOWN } },
                { DOWN, new List<string> { RIGHT, DOWN, LEFT, UP } },
                { RIGHT, new List<string> { UP, RIGHT, DOWN, LEFT } },
                { LEFT, new List<string> { DOWN, LEFT, UP, RIGHT } }
            };
        }
    }

    public void Solve()
    {
        while (!IsPikachuBackAtTheStart())
        {
            List<string> priorityList = pika.priorities[pika.facing];
            pika.previous = (pika.x, pika.y);

            foreach (string priority in priorityList)
            {
                if (priority == RIGHT)
                {
                    if (PikachuCanGoRight())
                    {
                        pika.facing = RIGHT;
                        pika.x += 1;
                        break;
                    }
                }
                else if (priority == DOWN)
                {
                    if (PikachuCanGoDown())
                    {
                        pika.facing = DOWN;
                        pika.y += 1;
                        break;
                    }
                }
                else if (priority == LEFT)
                {
                    if (PikachuCanGoLeft())
                    {
                        pika.facing = LEFT;
                        pika.x -= 1;
                        break;
                    }
                }
                else if (priority == UP)
                {
                    if (PikachuCanGoUp())
                    {
                        pika.facing = UP;
                        pika.y -= 1;
                        break;
                    }
                }
            }

            if (pika.IsTrapped())
            {
                break;
            }
            rows[pika.y][pika.x] = (int.Parse(rows[pika.y][pika.x]) + 1).ToString();
        }
    }

    public bool IsPikachuBackAtTheStart()
    {
        return (pika.x, pika.y) == pika.start && rows[pika.y][pika.x] != "0";
    }

    public bool PikachuCanGoDown()
    {
        return pika.y < height - 1 && rows[pika.y + 1][pika.x] != WALL.ToString();
    }

    public bool PikachuCanGoLeft()
    {
        return pika.x > 0 && rows[pika.y][pika.x - 1] != WALL.ToString();
    }

    public bool PikachuCanGoRight()
    {
        return pika.x < width - 1 && rows[pika.y][pika.x + 1] != WALL.ToString();
    }

    public bool PikachuCanGoUp()
    {
        return pika.y > 0 && rows[pika.y - 1][pika.x] != WALL.ToString();
    }

    public void PrintSolution()
    {
        for (int y = 0; y < height; y++)
        {
            for (int x = 0; x < width; x++)
            {
                Console.Write(rows[y][x]);
            }
            Console.WriteLine();
        }
    }
}

class Program
{
    static void Main(string[] args)
    {
        Game game = new Game();
        game.ReadInput();
        game.Solve();
        game.PrintSolution();
    }
}
