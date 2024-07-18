using System;

namespace Softcode
{
    class MainClass
    {
        /// <summary>
        /// Entry point of the program.
        /// Reads an integer from the user and counts how many times 
        /// it can be divided by 3 completely.
        /// </summary>
        /// <param name="args">Command-line arguments.</param>
        public static void Main(string[] args)
        {
            // Prompt the user to enter an integer
            Console.WriteLine("Enter integer number: ");
            int a = Convert.ToInt32(Console.ReadLine());
            
            // Initialize a counter to count the number of times the number is divisible by 3
            int cnt = 0;

            // Loop to divide the number by 3 as long as it is completely divisible by 3
            while (a % 3 == 0)
            {
                a = a / 3; // Divide the number by 3
                cnt++;     // Increment the counter
            }

            // Output the count of how many times the number was divisible by 3
            Console.WriteLine(cnt);
        }
    }
}
