using System;

class Solution
{
    static int[] registers;
    static string[] instructions;
    static int curLine = 0;
    const string names = "abcd";

    static void Main(string[] args)
    {
        const int NB_REGISTERS = 4;
        var inStr = Console.ReadLine();
        var inArr = inStr.Split(' ');
        registers = new int[NB_REGISTERS];
        for (int i = 0; i < NB_REGISTERS; ++i)
            registers[i] = int.Parse(inArr[i]);

        int nbLines = int.Parse(Console.ReadLine());
        instructions = new string[nbLines];
        for (int i = 0; i < nbLines; ++i)
            instructions[i] = Console.ReadLine();

        do
        {
            string line = instructions[curLine];
            interpret(line);
            Console.Error.WriteLine(curLine + " " + line);
            // printRegisters();
        } while (curLine != nbLines);

        string output = "";
        foreach (int register in registers)
            output += register.ToString() + " ";

        Console.WriteLine(output.Trim());
    }

    static void interpret(string line)
    {
        string[] instruction = line.Split(' ');
        switch (instruction[0])
        {
            case "MOV": move(instruction); ++curLine; break;
            case "ADD": add(instruction); ++curLine; break;
            case "SUB": sub(instruction); ++curLine; break;
            case "JNE": jumpNotEqual(instruction); break;
        }
    }

    static void move(string[] instruction)
    {
        int dest = index(instruction[1]);
        string value = instruction[2];
        if (names.Contains(value))
        {
            int source = index(value);
            registers[dest] = registers[source];
        }
        else
        {
            registers[dest] = int.Parse(value);
        }
    }

    static void operation(string[] instruction, int sign)
    {
        int result;

        int dest = index(instruction[1]);
        string value = instruction[2];
        if (names.Contains(value))
        {
            int source = index(value);
            result = registers[source];
        }
        else
        {
            result = int.Parse(value);
        }

        value = instruction[3];
        if (names.Contains(value))
        {
            int source = index(value);
            result += sign * registers[source];
        }
        else
        {
            result += sign * int.Parse(value);
        }

        registers[dest] = result;
    }

    static void add(string[] instruction)
    {
        operation(instruction, 1);
    }

    static void sub(string[] instruction)
    {
        operation(instruction, -1);
    }

    static void jumpNotEqual(string[] instruction)
    {
        int operand1 = registers[index(instruction[2])];
        int operand2;
        string value2 = instruction[3];
        if (names.Contains(value2))
            operand2 = registers[index(value2)];
        else
            operand2 = int.Parse(value2);

        if (operand1 != operand2)
            curLine = int.Parse(instruction[1]);
        else
            ++curLine;
    }

    static int index(string register)
    {
        return char.ToLower(register[0]) - 'a';
    }

    static void printRegisters()
    {
        string output = "";
        foreach (int register in registers)
            output += register.ToString() + " ";

        Console.Error.WriteLine(output.Trim());
    }
}
