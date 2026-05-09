using System;
using System.Collections.Generic;

class Program
{
    static void Main(string[] args)
    {
        Dictionary<string, string> table = new Dictionary<string, string>(); // file extension => mime type
        int nb_elements = int.Parse(Console.ReadLine());
        int nb_names = int.Parse(Console.ReadLine());

        for (int i = 0; i < nb_elements; i++)
        {
            string[] input = Console.ReadLine().Split();
            string extension = input[0].ToLower();
            string mime_type = input[1];
            table[extension] = mime_type;
        }

        for (int i = 0; i < nb_names; i++)
        {
            string name = Console.ReadLine().ToLower();
            int dot_index = name.LastIndexOf(".");
            
            if (dot_index == -1 || dot_index == name.Length - 1)
            {
                Console.WriteLine("UNKNOWN");
            }
            else
            {
                string extension = name.Substring(dot_index + 1);
                
                if (table.ContainsKey(extension))
                {
                    Console.WriteLine(table[extension]);
                }
                else
                {
                    Console.WriteLine("UNKNOWN");
                }
            }
        }
    }
}
