using System;

namespace Softcode
{
    class MainClass
    {
        /// <summary>
        /// This program calculates the number of even numbers in a given range.
        /// </summary>
        public static void Main(string[] args)
        {
            // Ask the user to enter the first integer number
            Console.WriteLine("Enter the first integer number, please: ");
            int x = Convert.ToInt32(Console.ReadLine());

            // Ask the user to enter the second integer number
            Console.WriteLine("Enter the second integer number, please: ");
            int y = Convert.ToInt32(Console.ReadLine());

            int count = 0;

            // Loop through the range from x to y (inclusive) and count the even numbers
            for (; x <= y; x++)
            {
                if (x % 2 == 0)
                {
                    count++;
                }
            }

            // Output the total count of even numbers in the given range
            Console.WriteLine();
            Console.Write("Total even numbers in the given range: ");
            Console.WriteLine(count);
        }
    }
}
