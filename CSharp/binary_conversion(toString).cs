using System;

namespace Softcode
{
    class MainClass
    {
        /// <summary>
        /// Main entry point of the program. Converts an integer number to its binary representation.
        /// </summary>
        /// <param name="args">Command-line arguments (not used in this program).</param>
        public static void Main(string[] args)
        {
            Console.WriteLine("Enter an integer number: ");
            int number = Convert.ToInt32(Console.ReadLine());

            // Use the Convert.ToString method with base 2 to convert the number to binary representation.
            string binValue = Convert.ToString(number, 2);

            // Display the binary representation of the input number.
            Console.WriteLine(binValue);
        }
    }
}
