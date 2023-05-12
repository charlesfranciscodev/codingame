using System;
using System.Collections.Generic;

public class Program
{
    // letter => points
    static Dictionary<char, int> MAPPING = new Dictionary<char, int>()
    {
        {'e', 1}, {'a', 1}, {'i', 1}, {'o', 1}, {'n', 1}, {'r', 1}, {'t', 1}, {'l', 1}, {'s', 1}, {'u', 1},
        {'d', 2}, {'g', 2},
        {'b', 3}, {'c', 3}, {'m', 3}, {'p', 3},
        {'f', 4}, {'h', 4}, {'v', 4}, {'w', 4}, {'y', 4},
        {'k', 5},
        {'j', 8}, {'x', 8},
        {'q', 10}, {'z', 10}
    };

    public static bool IsValidWord(List<char> word, List<char> letters)
    {
        foreach (char c in word)
        {
            if (!letters.Contains(c))
                return false;
            else
                letters.Remove(c);
        }
        return true;
    }

    public static int CalculateScore(List<char> word)
    {
        int totalScore = 0;
        foreach (char c in word)
        {
            totalScore += MAPPING[c];
        }
        return totalScore;
    }

    public static string Solve(List<string> words, string letters)
    {
        int bestScore = 0;
        string bestWord = "";
        foreach (string word in words)
        {
            List<char> lettersCopy = new List<char>(letters.ToCharArray());
            if (IsValidWord(new List<char>(word), lettersCopy))
            {
                int currentScore = CalculateScore(new List<char>(word));
                if (currentScore > bestScore)
                {
                    bestScore = currentScore;
                    bestWord = word;
                }
            }
        }
        return bestWord;
    }

    public static void Main()
    {
        // read game input
        List<string> words = new List<string>();
        int nbWords = int.Parse(Console.ReadLine());
        for (int i = 0; i < nbWords; i++)
        {
            words.Add(Console.ReadLine());
        }
        string letters = Console.ReadLine();

        Console.WriteLine(Solve(words, letters));
    }
}
