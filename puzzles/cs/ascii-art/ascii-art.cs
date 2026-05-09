using System;

class Program
{
    static void Main(string[] args)
    {
        int width = int.Parse(Console.ReadLine());
        int height = int.Parse(Console.ReadLine());
        string text = Console.ReadLine().ToUpper();

        for (int i = 0; i < height; i++)
        {
            string row = Console.ReadLine();
            string output = "";

            foreach (char character in text)
            {
                int position = character - 'A';

                if (position < 0 || position > 25)
                    position = 26;

                int start = position * width;
                int end = start + width;
                output += row.Substring(start, width);
            }

            Console.WriteLine(output);
        }
    }
}
