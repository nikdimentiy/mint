// the code calculate: how many even numbers on a given range
using System;

namespace Softcode
{
    class MainClass
    {
        public static void Main(string[] args)
        {
            Console.WriteLine("Enter the first integer number, please: ");
            int x = Convert.ToInt32(Console.ReadLine());

            Console.WriteLine("Enter the second integer number, please: ");
            int y = Convert.ToInt32(Console.ReadLine());

            int count = 0;

            for (; x <= y; x++)
                if (x % 2 == 0)
                {
                    count++;
                }
            Console.WriteLine();
            Console.Write("Total even numbers a given range: ");
            Console.WriteLine(count);
        }
    }
}

