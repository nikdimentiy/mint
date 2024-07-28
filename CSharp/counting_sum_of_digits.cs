// This program calculates the sum of digits in an integer number.

using System;

namespace Softcode
{
    class MainClass
    {
        /// <summary>
        /// Main method to calculate the sum of digits in an integer number.
        /// </summary>
        /// <param name="args">Command-line arguments</param>
        public static void Main(string[] args)
        {
            // Prompt the user to enter an integer number
            Console.WriteLine("Enter an integer number: ");
            int n = Convert.ToInt32(Console.ReadLine());

            int sum = 0; // Initialize a variable to store the sum of digits

            // Loop to extract and sum each digit of the number
            while (n > 0)
            {
                int digit = n % 10; // Get the last digit of the number
                sum += digit; // Add the digit to the sum
                n = n / 10; // Remove the last digit from the number
            }

            // Display the sum of digits
            Console.WriteLine("The sum of digits in the number is: " + sum);
        }
    }
}
