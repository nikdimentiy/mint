using System;

namespace Chess
{
    /// <summary>
    /// This program checks if a chess cell is within the attack range of a king on a chessboard.
    /// </summary>
    class MainClass
    {
        /// <summary>
        /// Main method to execute the program.
        /// </summary>
        public static void Main(string[] args)
        {
            Console.WriteLine("Enter the king coordinates: ");
            int kingRow, kingColumn;

            Console.WriteLine("Enter row of the king: ");
            kingRow = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Enter column of the king: ");
            kingColumn = Convert.ToInt32(Console.ReadLine());

            Console.WriteLine("Enter coordinates of the chess cell");
            int cellRow, cellColumn;

            Console.WriteLine("Enter row of the chess cell:");
            cellRow = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Enter column of the chess cell:");
            cellColumn = Convert.ToInt32(Console.ReadLine());

            // Check if the chess cell is within the attack range of the king
            if (Math.Abs(kingRow - cellRow) <= 1 && Math.Abs(kingColumn - cellColumn) <= 1)
            {
                Console.WriteLine("The chess cell is within the attack range of the king: YES");
            }
            else
            {
                Console.WriteLine("The chess cell is not within the attack range of the king: NO");
            }

            Console.ReadKey();
        }
    }
}
