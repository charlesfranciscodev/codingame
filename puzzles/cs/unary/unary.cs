using System;

class Program
{
    static string ToBinary(string text)
    {
        string binaryText = "";
        foreach (char character in text)
        {
            binaryText += Convert.ToString(character, 2).PadLeft(7, '0');
        }
        return binaryText;
    }

    static string ToUnary(string text)
    {
        string unaryText = "";
        bool prevDigit = false; // False = 0, True = 1
        
        // Handle first character
        if (text.Length >= 1)
        {
            if (text[0] == '0')
            {
                unaryText += "00 0";
            }
            else
            {
                unaryText += "0 0";
                prevDigit = true;
            }
        }

        for (int i = 1; i < text.Length; i++)
        {
            if (text[i] == '0' && prevDigit)
            {
                unaryText += " 00 0"; // Switch from 1 to 0
                prevDigit = false;
            }
            else if (text[i] == '1' && !prevDigit)
            {
                unaryText += " 0 0"; // Switch from 0 to 1
                prevDigit = true;
            }
            else
            {
                unaryText += "0"; // Repeat digit
            }
        }
        return unaryText;
    }

    static void Main(string[] args)
    {
        string text = Console.ReadLine();
        string binaryText = ToBinary(text);
        string unaryText = ToUnary(binaryText);
        Console.WriteLine(unaryText);
    }
}
