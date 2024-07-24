using System;

namespace Softcode
{
    /// <summary>
    /// This program determines if a knight in a chess game can attack a given chess piece based on coordinates.
    /// </summary>
    class MainClass
    {
        /// <summary>
        /// Main method to get user input for knight and chess piece coordinates and check for possible attack.
        /// </summary>
        public static void Main(string[] args)
        {
            // Prompt the user to enter the knight's coordinates
            Console.WriteLine("Enter the knight coordinates: ");
            int row1, column1;

            // Read the row and column of the knight from the user
            Console.WriteLine("Enter row of the knight: ");
            row1 = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Enter column of the knight: ");
            column1 = Convert.ToInt32(Console.ReadLine());

            // Prompt the user to enter the chess piece coordinates
            Console.WriteLine("Enter coordinates of the chess piece");
            int row2, column2;

            // Read the row and column of the chess piece from the user
            Console.WriteLine("Enter row of the chess piece:");
            row2 = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Enter column of the chess piece:");
            column2 = Convert.ToInt32(Console.ReadLine());

            // Calculate the distance between the knight and the chess piece using Euclidean distance formula
            if (Math.Sqrt(Math.Pow((row2 - row1), 2) + Math.Pow((column2 - column1), 2)) == Math.Sqrt(5))
            {
                Console.WriteLine("YES");
            }
            else
            {
                Console.WriteLine("NO");
            }
        }
    }
}
