// queen move (chess - possible attack)

using System;

namespace Softcode
{
    class MainClass
    {
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

            Console.Write(row1 == row2 || column1 == column2 || Math.Abs(row1 - row2) == Math.Abs(column1 - column2) ? "YES" : "NO");

            Console.ReadKey();
        }
    }
}