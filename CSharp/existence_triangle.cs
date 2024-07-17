using System;

namespace Softcode
{
    /// <summary>
    /// This program checks if it's possible to form a triangle with the given side lengths.
    /// </summary>
    class MainClass
    {
        /// <summary>
        /// Main method to execute the program.
        /// </summary>
        public static void Main(string[] args)
        {
            // Prompt the user to enter the first side of the triangle
            Console.WriteLine("Enter the first side of the triangle: ");
            int a = Convert.ToInt32(Console.ReadLine());

            // Prompt the user to enter the second side of the triangle
            Console.WriteLine("Enter the second side of the triangle: ");
            int b = Convert.ToInt32(Console.ReadLine());

            // Prompt the user to enter the third side of the triangle
            Console.WriteLine("Enter the third side of the triangle: ");
            int c = Convert.ToInt32(Console.ReadLine());

            // Check if the given sides can form a triangle
            if ((a < (b + c)) && (b < (a + c)) && (c < (a + b))) // Basic conditions for a triangle
            {
                Console.WriteLine("YES, a triangle can be formed.");
            }
            else
            {
                Console.WriteLine("NO, a triangle cannot be formed with the given side lengths.");
            }
        }
    }
}
