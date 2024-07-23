using System;

namespace Softcode
{
    /// <summary>
    /// This program checks if a queen in a chess game can attack a given chess piece based on their coordinates.
    /// </summary>
    class MainClass
    {
        /// <summary>
        /// Main method where the program execution starts.
        /// </summary>
        /// <param name="args">Command-line arguments</param>
        public static void Main(string[] args)
        {
            Console.WriteLine("Enter the queen coordinates: ");
            int row1, column1;

            Console.WriteLine("Enter row of the queen: ");
            row1 = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Enter column of the queen: ");
            column1 = Convert.ToInt32(Console.ReadLine());

            Console.WriteLine("Enter coordinates of the chess piece");
            int row2, column2;

            Console.WriteLine("Enter row of the chess piece:");
            row2 = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Enter column of the chess piece:");
            column2 = Convert.ToInt32(Console.ReadLine());

            // Check if the queen can attack the given chess piece based on their coordinates
            if ((Math.Abs(row1 - row2) == Math.Abs(column1 - column2)) || (((row1 == row2) && (column1 != column2)) || ((row1 != row2) && (column1 == column2))))
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
