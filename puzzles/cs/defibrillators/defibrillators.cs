using System;

public class Program
{
    public static double hypo(double x, double y)
    {
        return Math.Sqrt(Math.Pow(x, 2) + Math.Pow(y, 2));
    }

    public static double ToRadians(string angleInDegrees)
    {
        return Convert.ToDouble(angleInDegrees.Replace(",", ".")) * Math.PI / 180;
    }

    public static void Main()
    {
        double minDistance = double.PositiveInfinity;
        string closestDefibName = "";
        double longitude = ToRadians(Console.ReadLine());
        double latitude = ToRadians(Console.ReadLine());
        int nbDefib = int.Parse(Console.ReadLine());

        for (int i = 0; i < nbDefib; i++)
        {
            string[] defib = Console.ReadLine().Split(';');
            double defibLongitude = ToRadians(defib[4]);
            double defibLatitude = ToRadians(defib[5]);
            double x = (defibLongitude - longitude) * Math.Cos((latitude + defibLatitude) / 2);
            double y = defibLatitude - latitude;
            int EARTH_RADIUS = 6371;
            double distance = hypo(x, y) * EARTH_RADIUS;
            if (distance < minDistance)
            {
                minDistance = distance;
                closestDefibName = defib[1];
            }
        }

        Console.WriteLine(closestDefibName);
    }
}
