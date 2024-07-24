using System;

namespace Softcode
{
    /// <summary>
    /// This program calculates the next even number of the entered number.
    /// </summary>
    class MainClass
    {
        /// <summary>
        /// Main method to get user input and calculate the next even number.
        /// </summary>
        public static void Main(string[] args)
        {
            // Prompt the user to enter a number
            Console.WriteLine("Enter your number: ");

            // Read the input number from the user
            int n = Convert.ToInt32(Console.ReadLine());

            // Calculate and display the next even number
            Console.Write(n + 2 - n % 2);
        }
    }
}
