# CONWAY SEQUENCE

## C# Code Documentation

```csharp
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
```

### Description

The code provided demonstrates the generation of a Conway Sequence. The Conway Sequence is a sequence of numbers in which each line describes the previous line. The program reads an input number (`original`) from the console, as well as the line number (`lineNumber`) indicating the desired line of the Conway Sequence. The program then generates and outputs the corresponding line of the Conway Sequence.

### Method

The program consists of a single method:

#### `Main()`

This method serves as the entry point for the program execution. It performs the following steps:

1. Reads the input number `original` from the console using `Console.ReadLine()`.
2. Reads the line number `lineNumber` from the console using `Console.ReadLine()`.
3. Creates a `List<int>` named `conwaySequence` and adds `original` to it.
4. Executes a loop that iterates from `1` to `lineNumber - 1` to generate the remaining lines of the Conway Sequence.
    - Within the loop, a new `List<int>` named `tempSequence` is created to store the numbers of the current line.
    - Two variables, `count` and `previous`, are initialized to `0` and the first element of `conwaySequence`, respectively.
    - A nested loop iterates over each number in `conwaySequence` and checks if it is the same as the previous number.
    - If the number is the same, `count` is incremented. Otherwise, the count and previous number are added to `tempSequence`, and `count` and `previous` are updated.
    - After the nested loop finishes, the final `count` and `previous` are added to `tempSequence`.
    - The `conwaySequence` is then updated with the `tempSequence` for the next iteration.
5. Finally, the program outputs the Conway Sequence for the desired line by joining the numbers with spaces using `string.Join()` and printing the result using `Console.WriteLine()`.

The provided code calculates the Conway Sequence efficiently using a list to store the numbers of each line. The sequence is updated iteratively by appending the generated numbers for each line.

Please note that this documentation assumes some familiarity with the Conway Sequence and focuses on explaining the structure and purpose of the code.