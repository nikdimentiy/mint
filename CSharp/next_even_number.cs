using System;

namespace Softcode
{
    class MainClass
    {
        /// <summary>
        /// This program calculates the next even number of the entered number.
        /// If the entered number is even, it adds 2 to get the next even number.
        /// If the entered number is odd, it adds 1 to get the next even number.
        /// </summary>
        public static void Main(string[] args)
        {
            // Prompt the user to enter a number
            Console.WriteLine("Enter your number: ");

            // Read the input from the user and convert it to a double
            double n;
            if (double.TryParse(Console.ReadLine(), out n))
            {
                // Check if the number is even
                if (n % 2 == 0)
                {
                    // If even, add 2 to get the next even number
                    Console.WriteLine(n + 2);
                }
                else
                {
                    // If odd, add 1 to get the next even number
                    Console.WriteLine(n + 1);
                }
            }
            else
            {
                // Handle invalid input
                Console.WriteLine("Invalid input. Please enter a valid number.");
            }
        }
    }
}
