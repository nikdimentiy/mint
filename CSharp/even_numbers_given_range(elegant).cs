// even numbers on a given range (elegant version)
using System;

namespace Softcode
{
    class MainClass
    {
        public static void Main(string[] args)
        {
            Console.WriteLine("Enter the first integer number, please: ");
            int x = Convert.ToInt32(Console.ReadLine());

            Console.WriteLine("Enter the second integer number, please:");
            int y = Convert.ToInt32(Console.ReadLine());

            int cnt = 0;
            
            Console.WriteLine();
            Console.WriteLine("Even numbers in range: ");

            for (int i = x + x % 2; i <= y; i += 2)
            {
                Console.WriteLine(i);
                cnt++;
            }
            Console.WriteLine("____________________________________");
            Console.WriteLine("Total even numbers a given range: " + cnt);
        }
    }
}


