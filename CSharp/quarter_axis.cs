using System;

namespace Softcode
{
    /// <summary>
    /// This program determines the quadrant in which a point lies in a Cartesian coordinate system based on the provided x and y coordinates.
    /// It outputs the quadrant number (1, 2, 3, or 4) to the console.
    /// </summary>
    class MainClass
    {
        public static void Main(string[] args)
        {
            Console.WriteLine("Give me the x-coordinate: ");
            double x = Convert.ToDouble(Console.ReadLine());

            Console.WriteLine("Give me the y-coordinate: ");
            double y = Convert.ToDouble(Console.ReadLine());

            // Determine the quadrant based on the signs of x and y
            if (x > 0 && y > 0)
            {
                Console.WriteLine("Quadrant: 1");
            }

            if (x < 0 && y > 0)
            {
                Console.WriteLine("Quadrant: 2");
            }

            if (x < 0 && y < 0)
            {
                Console.WriteLine("Quadrant: 3");
            }

            if (x > 0 && y < 0)
            {
                Console.WriteLine("Quadrant: 4");
            }
        }
    }
}
