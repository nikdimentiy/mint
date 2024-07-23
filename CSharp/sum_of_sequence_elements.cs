using System;

namespace Softcode
{
    /// <summary>
    /// This program calculates the sum of a sequence of numbers that are multiples of 2 but not multiples of 3.
    /// </summary>
    class MainClass
    {
        /// <summary>
        /// Main method where the program execution starts.
        /// </summary>
        /// <param name="args">Command-line arguments</param>
        public static void Main(string[] args)
        {
            Console.WriteLine("Enter integer numbers (enter 0 to finish): ");
            int n = Convert.ToInt32(Console.ReadLine());

            int sum = 0;

            // Loop to calculate the sum of numbers meeting the condition
            while (n != 0) // Entering 0 terminates the input process
            {
                if (n % 2 == 0 && n % 3 != 0)
                    sum += n;
                
                n = Convert.ToInt32(Console.ReadLine());
            }

            Console.WriteLine();
            Console.Write("The sum of entered numbers that meet the condition is: ");
            Console.WriteLine(sum);
        }
    }
}
