using System;

class Player
{
    // Define constants for better readability and maintainability
    const int MAX_VERTICAL_SPEED = -40;  // Maximum allowed vertical speed before adjusting thrust
    const int MAX_THRUST_POWER = 4;      // Maximum thrust power
    const int MIN_THRUST_POWER = 0;      // Minimum thrust power

    static void Main(string[] args)
    {
        string[] inputs;
        int surfaceN = int.Parse(Console.ReadLine()); // the number of points used to draw the surface of Mars.
        for (int i = 0; i < surfaceN; i++)
        {
            inputs = Console.ReadLine().Split(' ');
            int landX = int.Parse(inputs[0]); // X coordinate of a surface point. (0 to 6999)
            int landY = int.Parse(inputs[1]); // Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
        }

        // game loop
        while (true)
        {
            inputs = Console.ReadLine().Split(' ');
            int hSpeed = int.Parse(inputs[2]); // the horizontal speed (in m/s), can be negative.
            int vSpeed = int.Parse(inputs[3]); // the vertical speed (in m/s), can be negative.
            int power = int.Parse(inputs[6]); // the thrust power (0 to 4).

            // Adjust thrust power based on the vertical speed using constants
            if (vSpeed <= MAX_VERTICAL_SPEED && power < MAX_THRUST_POWER) // Increase thrust if falling too fast
            {
                power++;
            }
            else if (vSpeed > MAX_VERTICAL_SPEED && power > MIN_THRUST_POWER) // Decrease thrust if falling slowly
            {
                power--;
            }

            // Output the desired rotation and power (rotation is always 0 for this level)
            Console.WriteLine("0 " + power);
        }
    }
}
