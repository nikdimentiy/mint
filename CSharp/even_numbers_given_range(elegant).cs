using System;

namespace Softcode
{
    /// <summary>
    /// This program takes two integer inputs and prints all even numbers within the given range.
    /// </summary>
    class MainClass
    {
        /// <summary>
        /// Main method to execute the program.
        /// </summary>
        public static void Main(string[] args)
        {
            Console.WriteLine("Enter the first integer number, please: ");
            int x = Convert.ToInt32(Console.ReadLine());

            Console.WriteLine("Enter the second integer number, please:");
            int y = Convert.ToInt32(Console.ReadLine());

            int cnt = 0;
            
            Console.WriteLine();
            Console.WriteLine("Even numbers in range: ");

            // Loop through the range to find and print even numbers
            for (int i = x + x % 2; i <= y; i += 2)
            {
                Console.WriteLine(i);
                cnt++;
            }
            Console.WriteLine("____________________________________");
            Console.WriteLine("Total even numbers in the given range: " + cnt);
        }
    }
}
