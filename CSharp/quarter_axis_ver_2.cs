// This program determines the quarter of the coordinate system based on the input x and y values.

using System;

namespace Softcode 
{
    class MainClass
    {
        /// <summary>
        /// Main method to determine the quarter of the coordinate system based on input x and y values.
        /// </summary>
        /// <param name="args">Command-line arguments</param>
        public static void Main(string[] args)
        {
            // Input x and y values
            Console.WriteLine("Enter the value of x:");
            double x = Convert.ToDouble(Console.ReadLine());

            Console.WriteLine("Enter the value of y:");
            double y = Convert.ToDouble(Console.ReadLine());

            // Determine the quarter based on x and y values
            if (x > 0)
            {
                if (y > 0)
                {
                    Console.WriteLine("The point is in the first quarter (Q1).");
                }
                else
                {
                    Console.WriteLine("The point is in the fourth quarter (Q4).");
                }
            }
            else
            {
                if (y > 0)
                {
                    Console.WriteLine("The point is in the second quarter (Q2).");
                }
                else
                {
                    Console.WriteLine("The point is in the third quarter (Q3).");
                }
            }
        }
    }
}
