using System;

namespace Softcode
{
    /// <summary>
    /// This program calculates the product of numbers on the segment from a to b, ending in 7.
    /// </summary>
    class MainClass
    {
        /// <summary>
        /// Main method where the program execution starts.
        /// </summary>
        public static void Main(string[] args)
        {
            // Prompt the user to enter the first integer number.
            Console.WriteLine("Enter the first integer number: ");
            int a = Convert.ToInt32(Console.ReadLine());

            // Prompt the user to enter the second integer number.
            Console.WriteLine("Enter the second integer number: ");
            int b = Convert.ToInt32(Console.ReadLine());

            // Initialize the product of the segment to 1.
            int productSegment = 1;

            // Loop through the numbers from a to b and calculate the product of numbers ending in 7.
            for (int i = a; i <= b; i++)
            {
                if (i % 10 == 7)
                {
                    productSegment *= i;
                }
            }

            // Display the result to the user.
            Console.WriteLine("The product of numbers on the segment from " 
                             + a + " to " + b + " ending in 7 is: " + productSegment);
        }
    }
}
