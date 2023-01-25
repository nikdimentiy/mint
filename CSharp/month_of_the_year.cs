//the tiny code - switch_case (month of the year) 
using System;

namespace Softcode
{
    class MainClass
    {
        public static void Main(string[] args)
        {
            Console.WriteLine("Enter your favorite month (number): ");
            int a = Convert.ToInt32(Console.ReadLine());
            a = a / 3;
            switch (a)
            {
                case (0): Console.WriteLine("Winter"); break;
                case (4): Console.WriteLine("Winter"); break;
                case (1): Console.WriteLine("Spring"); break;
                case (2): Console.WriteLine("Summer"); break;
                case (3):
                    Console.WriteLine("Fall"); break;
            }
        }
    }
}

