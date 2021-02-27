// king move in chess cell (the possibility of attack)

using System;

namespace Prime
{
    class MainClass
    {
        public static void Main(string[] args)
        {
            Console.WriteLine("Enter the king coordinates: ");
            int row1, column1;

            Console.WriteLine("Enter row of the king: ");
            row1 = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Enter column of the king: ");
            column1 = Convert.ToInt32(Console.ReadLine());


            Console.WriteLine("Enter coordinates of the chess cell");
            int row2, column2;

            Console.WriteLine("Enter row of the chess cell:");
            row2 = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Enter column of the chess cell:");
            column2 = Convert.ToInt32(Console.ReadLine());

            if (Math.Abs(row1 - column1) <= 1 && Math.Abs(row2 - column2) <= 1)
            {
                Console.WriteLine("YES");
            }
            else
            {
                Console.WriteLine("NO");
            }

            Console.ReadKey();
        }
    }
}
