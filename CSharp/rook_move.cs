using System;

namespace Softcode
{
    /// <summary>
    /// This program determines if a rook in chess can attack a given chess piece based on their coordinates.
    /// </summary>
    class MainClass
    {
        /// <summary>
        /// Main method where the program execution starts.
        /// </summary>
        public static void Main(string[] args)
        {
            // Prompt the user to enter the rook's coordinates.
            Console.WriteLine("Enter rook coordinates");
            int row1, column1;

            // Prompt the user to enter the row of the rook.
            Console.WriteLine("Enter row of the rook:");
            row1 = Convert.ToInt32(Console.ReadLine());

            // Prompt the user to enter the column of the rook.
            Console.WriteLine("Enter column of the rook:");
            column1 = Convert.ToInt32(Console.ReadLine());

            // Prompt the user to enter the coordinates of the chess piece.
            Console.WriteLine("Enter coordinates of the chess piece");
            int row2, column2;

            // Prompt the user to enter the row of the chess piece.
            Console.WriteLine("Enter row of the chess piece:");
            row2 = Convert.ToInt32(Console.ReadLine());

            // Prompt the user to enter the column of the chess piece.
            Console.WriteLine("Enter column of the chess piece:");
            column2 = Convert.ToInt32(Console.ReadLine());

            // Check if the rook can attack the chess piece based on their coordinates.
            if (((row1 == row2) && (column1 != column2)) || ((row1 != row2) && (column1 == column2)))
            {
                Console.WriteLine("YES"); // Rook can attack
            }
            else
            {
                Console.WriteLine("NO"); // Rook cannot attack
            }
        }
    }
}
