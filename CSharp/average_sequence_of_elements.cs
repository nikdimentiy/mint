using System;

namespace Softcode
{
    class MainClass
    {
        /// <summary>
        /// Main entry point of the program. Calculates the arithmetic mean of a sequence of integers.
        /// </summary>
        /// <param name="args">Command-line arguments (not used in this program).</param>
        public static void Main(string[] args)
        {
            Console.WriteLine("Enter integer numbers to create a sequence:");
            Console.WriteLine("To terminate input, please enter (zero).");

            int n = Convert.ToInt32(Console.ReadLine());
            double sum = 0;
            int count = 0;

            // Continue to input numbers until the user enters 0.
            while (n != 0)
            {
                sum += n; // Add the entered number to the sum.
                n = Convert.ToInt32(Console.ReadLine()); // Prompt for the next number.
                count++; // Increase the count of entered numbers.
            }

            // Calculate the arithmetic mean (average) of the sequence.
            double result = sum / count;

            Console.WriteLine();
            Console.Write("The arithmetic mean of the elements of the sequence is: ");
            Console.WriteLine(result);
        }
    }
}
