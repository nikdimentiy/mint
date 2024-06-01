using System;

namespace Softcode
{
    class MainClass
    {
        /// <summary>
        /// The entry point of the program which calculates the power of 2 for a given integer.
        /// </summary>
        /// <param name="args">The command-line arguments.</param>
        public static void Main(string[] args)
        {
            // Prompt the user to enter an integer number
            Console.WriteLine("Enter integer number: ");
            
            // Read the user input and convert it to an integer
            int n;
            while (!int.TryParse(Console.ReadLine(), out n))
            {
                Console.WriteLine("Invalid input. Please enter a valid integer number: ");
            }

            // Initialize power to 1 (2^0) and degree to 0
            int power = 1;
            int degree = 0;

            // Calculate 2^n using a while loop
            while (degree < n)
            {
                power *= 2;
                degree++;
            }

            // Output the result
            Console.WriteLine($"2^{n} = {power}");
        }
    }
}
