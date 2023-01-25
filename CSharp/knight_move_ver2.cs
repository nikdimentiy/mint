// knight move (chess - possible attack) - version 2
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

