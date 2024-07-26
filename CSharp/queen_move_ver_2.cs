*using System;

namespace Softcode
{
    class MainClass
    {
        /// <summary>
        /// This program checks if a queen in chess can attack a given chess piece based on their coordinates.
        /// </summary>
        public static void Main(string[] args)
        {
            // Get the coordinates of the queen
            Console.WriteLine("Enter the queen coordinates: ");
            int queenRow, queenColumn;

            Console.WriteLine("Enter row of the queen: ");
            queenRow = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Enter column of the queen: ");
            queenColumn = Convert.ToInt32(Console.ReadLine());

            // Get the coordinates of the chess piece
            Console.WriteLine("Enter coordinates of the chess piece");
            int pieceRow, pieceColumn;

            Console.WriteLine("Enter row of the chess piece:");
            pieceRow = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Enter column of the chess piece:");
            pieceColumn = Convert.ToInt32(Console.ReadLine());

            // Check if the queen can attack the chess piece
            bool canAttack = queenRow == pieceRow || queenColumn == pieceColumn || Math.Abs(queenRow - pieceRow) == Math.Abs(queenColumn - pieceColumn;

            // Output the result
            Console.WriteLine(canAttack ? "YES" : "NO");

            Console.ReadKey();
        }
    }
}
