// knight move (chess - possible attack)
using System;

namespace Softcode
{
    class MainClass
    {
        public static void Main(string[] args)
        {
            Console.WriteLine("Enter the knight coordinates: ");
            int row1, column1;

            Console.WriteLine("Enter row of the knight: ");
            row1 = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Enter column of the knight: ");
            column1 = Convert.ToInt32(Console.ReadLine());


            Console.WriteLine("Enter coordinates of the chess piece");
            int row2, column2;

            Console.WriteLine("Enter row of the chess piece:");
            row2 = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Enter column of the chess piece:");
            column2 = Convert.ToInt32(Console.ReadLine());

            if (Math.Abs(row1 - row2) == 2 && Math.Abs(column1 - column2) == 1 ||
                Math.Abs(row1 - row2) == 1 && Math.Abs(column1 - column2) == 2)
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
