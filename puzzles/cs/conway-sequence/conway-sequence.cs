using System;
using System.Collections.Generic;

public class Program
{
    public static void Main()
    {
        int original = int.Parse(Console.ReadLine());
        int lineNumber = int.Parse(Console.ReadLine());
        List<int> conwaySequence = new List<int> { original };

        for (int line = 1; line < lineNumber; line++)
        {
            List<int> tempSequence = new List<int>();
            int count = 0;
            int previous = conwaySequence[0];
            foreach (int number in conwaySequence)
            {
                if (number == previous)
                {
                    count += 1;
                }
                else
                {
                    tempSequence.Add(count);
                    tempSequence.Add(previous);
                    previous = number;
                    count = 1;
                }
            }

            tempSequence.Add(count);
            tempSequence.Add(previous);
            conwaySequence = tempSequence;  // update
        }

        Console.WriteLine(string.Join(" ", conwaySequence));
    }
}
