// rook move (chess - possible attack)
using System;

namespace Softcode
{
    class MainClass
    {
        public static void Main(string[] args)
        {
            Console.WriteLine("Enter rook coordinates");
            int row1, column1;

            Console.WriteLine("Enter row of the rook:");
            row1 = Convert.ToInt32(Console.ReadLine());

            Console.WriteLine("Enter column of the rook:");
            column1 = Convert.ToInt32(Console.ReadLine());

            Console.WriteLine("Enter coordinates of the chess piece");
            int row2, column2;

            Console.WriteLine("Enter row of the chess piece:");
            row2 = Convert.ToInt32(Console.ReadLine());

            Console.WriteLine("Enter column of the chess piece:");
            column2 = Convert.ToInt32(Console.ReadLine());

            if (((row1 == row2) && (column1 != column2)) || ((row1 != row2) && (column1 == column2)))
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
