using System;

namespace Softcode
{
    class MainClass
    {
        /// <summary>
        /// Converts a decimal integer to its binary representation.
        /// This method uses a cycle-based approach to perform the conversion.
        /// </summary>
        /// <param name="args">Command-line arguments (not used)</param>
        public static void Main(string[] args)
        {
            Console.WriteLine("Enter integer number: ");
            
            // Read user input and convert it to an integer
            if (!int.TryParse(Console.ReadLine(), out int n))
            {
                Console.WriteLine("Invalid input. Please enter a valid integer.");
                return;
            }

            // Handle negative numbers
            bool isNegative = n < 0;
            n = Math.Abs(n);

            // Variables to store the inverted binary representation and digit count
            int invertedNumberInBits = 0;
            int count = 0;

            // Convert decimal to binary (inverted)
            while (n > 0)
            {
                invertedNumberInBits = invertedNumberInBits * 10 + n % 2;
                n /= 2;
                count++;
            }

            // Print the binary representation
            if (isNegative)
            {
                Console.Write("-");
            }

            // Handle the case when input is 0
            if (count == 0)
            {
                Console.Write("0");
            }
            else
            {
                // Print the binary digits in correct order
                while (count > 0)
                {
                    Console.Write(invertedNumberInBits % 10);
                    invertedNumberInBits /= 10;
                    count--;
                }
            }

            Console.WriteLine(); // Add a newline for better formatting
        }
    }
}
