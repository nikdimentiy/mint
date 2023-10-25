using System;

namespace Softcode
{
    class MainClass
    {
        /// <summary>
        /// Main entry point of the program. Calculates the nth member of an arithmetic progression.
        /// </summary>
        /// <param name="args">Command-line arguments (not used in this program).</param>
        public static void Main(string[] args)
        {
            // Prompt the user to enter the first member of the arithmetic progression.
            Console.WriteLine("Enter the first member of the arithmetic progression: ");
            int a1 = Convert.ToInt32(Console.ReadLine());

            // Prompt the user to enter the common difference of the arithmetic progression.
            Console.WriteLine("Enter the difference of the arithmetic progression: ");
            int progressDifference = Convert.ToInt32(Console.ReadLine());

            // Prompt the user to enter the required member of the progression (n).
            Console.WriteLine("Enter the required member of the progression (n): ");
            int n = Convert.ToInt32(Console.ReadLine());

            // Calculate the nth member of the arithmetic progression using the formula:
            // an = a1 + (n - 1) * d, where an is the nth member, a1 is the first member, 
            // n is the required member, and d is the common difference.
            int result = a1 + progressDifference * (n - 1);

            // Display the calculated nth member of the arithmetic progression.
            Console.Write("The nth member of the arithmetic progression is: ");
            Console.WriteLine(result);
        }
    }
}


