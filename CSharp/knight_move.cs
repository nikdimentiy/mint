using System;

namespace Chess
{
    /// <summary>
    /// This program checks if a chess piece (knight) can attack a given chess cell based on its coordinates.
    /// </summary>
    class MainClass
    {
        /// <summary>
        /// Main method to execute the program.
        /// </summary>
        public static void Main(string[] args)
        {
            Console.WriteLine("Enter the knight coordinates: ");
            int knightRow, knightColumn;

            Console.WriteLine("Enter row of the knight: ");
            knightRow = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Enter column of the knight: ");
            knightColumn = Convert.ToInt32(Console.ReadLine());

            Console.WriteLine("Enter coordinates of the chess piece");
            int pieceRow, pieceColumn;

            Console.WriteLine("Enter row of the chess piece:");
            pieceRow = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Enter column of the chess piece:");
            pieceColumn = Convert.ToInt32(Console.ReadLine());

            // Check if the knight can attack the chess piece based on its movement pattern
            if ((Math.Abs(knightRow - pieceRow) == 2 && Math.Abs(knightColumn - pieceColumn) == 1) ||
                (Math.Abs(knightRow - pieceRow) == 1 && Math.Abs(knightColumn - pieceColumn) == 2))
            {
                Console.WriteLine("The knight can attack the chess piece: YES");
            }
            else
            {
                Console.WriteLine("The knight cannot attack the chess piece: NO");
            }
        }
    }
}
