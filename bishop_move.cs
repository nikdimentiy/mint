using System;

namespace ConsoleApplication1
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            Console.WriteLine("Enter bishop coordinates");
            int row1, column1;

            Console.WriteLine("Enter row of the bishop:");
            row1 = Convert.ToInt32(Console.ReadLine());

            Console.WriteLine("Enter column of the bishop:");
            column1 = Convert.ToInt32(Console.ReadLine());

            Console.WriteLine("Enter coordinates of the chess piece");
            int row2, column2;

            Console.WriteLine("Enter row of the chess piece:");
            row2 = Convert.ToInt32(Console.ReadLine());

            Console.WriteLine("Enter column of the chess piece:");
            column2 = Convert.ToInt32(Console.ReadLine());

            if (Math.Abs(row1 - row2) == Math.Abs(column1 - column2))
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