using System;

namespace MainClass
{
    /// <summary>
    /// This program calculates the distance between two points in a 2D coordinate system.
    /// </summary>
    class Hello
    {
        /// <summary>
        /// Main method to execute the program.
        /// </summary>
        static void Main()
        {
            // Prompt the user to enter the coordinates of the first point
            Console.WriteLine("Enter the coordinates of the first point: ");

            Console.Write("X1 = ");
            double x1 = Convert.ToDouble(Console.ReadLine());
            Console.Write("Y1 = ");
            double y1 = Convert.ToDouble(Console.ReadLine());

            // Prompt the user to enter the coordinates of the second point
            Console.WriteLine("Enter the coordinates of the second point: ");
            Console.Write("X2 = ");
            double x2 = Convert.ToDouble(Console.ReadLine());
            Console.Write("Y2 = ");
            double y2 = Convert.ToDouble(Console.ReadLine());

            // Calculate the horizontal and vertical distances
            double horizontalDistance = Math.Pow(x2 - x1, 2);
            double verticalDistance = Math.Pow(y2 - y1, 2);

            // Calculate the distance between the two points using the Pythagorean theorem
            double distance = Math.Sqrt(horizontalDistance + verticalDistance);

            // Display the calculated distance between the points
            Console.Write("Distance between the given points is: ");
            Console.WriteLine(distance);
        }
    }
}
