using System;

namespace Softcode
{
    /// <summary>
    /// This program checks if a given four-digit number is symmetric.
    /// A symmetric number is defined as a number where the first half is equal to the reversed second half.
    /// For example, 1221 is symmetric because 12 (first half) is equal to 21 (reversed second half).
    /// </summary>
    class MainClass
    {
        public static void Main(string[] args)
        {
            // Prompt the user to enter a four-digit number
            Console.WriteLine("Enter a four-digit number: ");
            int fourDigitNumber = Convert.ToInt32(Console.ReadLine());

            // Extract the first half and second half of the four-digit number
            int firsthalfOf4DigitNumber = fourDigitNumber / 100; // Get the first two digits
            int secondhalfOf4DigitNumber = (fourDigitNumber % 100); // Get the last two digits

            // Extract individual digits from the first half
            int a = firsthalfOf4DigitNumber / 10; // First digit of the first half
            int b = firsthalfOf4DigitNumber % 10;  // Second digit of the first half

            // Extract individual digits from the second half
            int c = secondhalfOf4DigitNumber / 10; // First digit of the second half
            int d = secondhalfOf4DigitNumber % 10;  // Second digit of the second half

            // Check if the number is symmetric
            if (b == c && a == d)
            {
                Console.WriteLine("YES"); // The number is symmetric
            }
            else
            {
                Console.WriteLine("NO"); // The number is not symmetric
            }
        }
    }
}
