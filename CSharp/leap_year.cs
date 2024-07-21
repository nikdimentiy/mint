using System;

namespace Softcode
{
    class MainClass
    {
        /// <summary>
        /// This program checks whether the entered year is a leap year (29 days in February).
        /// A year is a leap year if:
        /// 1. It is divisible by 4 and not divisible by 100, or
        /// 2. It is divisible by 400.
        /// </summary>
        public static void Main(string[] args)
        {
            // Prompt the user to enter a year
            Console.WriteLine("Enter the year you want to check: ");

            // Read the input from the user and convert it to an integer
            int year;
            if (int.TryParse(Console.ReadLine(), out year))
            {
                // Check if the year is a leap year
                if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0)
                {
                    // If it is a leap year, print "YES"
                    Console.WriteLine("YES");
                }
                else
                {
                    // If it is not a leap year, print "NO"
                    Console.WriteLine("NO");
                }
            }
            else
            {
                // Handle invalid input
                Console.WriteLine("Invalid input. Please enter a valid year.");
            }
        }
    }
}
