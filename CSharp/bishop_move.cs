using System;

namespace ConsoleApplication1
{
    internal class Program
    {
        /// <summary>
        /// The entry point of the program which determines if a bishop can attack a given piece in chess.
        /// </summary>
        /// <param name="args">The command-line arguments.</param>
        public static void Main(string[] args)
        {
            // Prompt the user to enter the bishop's coordinates
            Console.WriteLine("Enter bishop coordinates");

            // Declare variables for the bishop's row and column
            int row1, column1;

            // Prompt and read the row of the bishop from the user
            Console.WriteLine("Enter row of the bishop:");
            row1 = Convert.ToInt32(Console.ReadLine());

            // Prompt and read the column of the bishop from the user
            Console.WriteLine("Enter column of the bishop:");
            column1 = Convert.ToInt32(Console.ReadLine());

            // Prompt the user to enter the coordinates of the chess piece
            Console.WriteLine("Enter coordinates of the chess piece");

            // Declare variables for the piece's row and column
            int row2, column2;

            // Prompt and read the row of the chess piece from the user
            Console.WriteLine("Enter row of the chess piece:");
            row2 = Convert.ToInt32(Console.ReadLine());

            // Prompt and read the column of the chess piece from the user
            Console.WriteLine("Enter column of the chess piece:");
            column2 = Convert.ToInt32(Console.ReadLine());

            // Check if the bishop can attack the given piece
            // A bishop attacks diagonally, which means the absolute difference between
            // the rows and columns of the two pieces should be the same
            if (Math.Abs(row1 - row2) == Math.Abs(column1 - column2))
            {
                // If the condition is met, the bishop can attack the piece
                Console.WriteLine("YES");
            }
            else
            {
                // If the condition is not met, the bishop cannot attack the piece
                Console.WriteLine("NO");
            }
        }
    }
}
