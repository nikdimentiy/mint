// tiny code: calculates - next even number (of entered number)
using System;

namespace Softcode
{
    class MainClass
    {
        public static void Main(string[] args)
        {
            Console.WriteLine("Enter your number: ");
            double n = Convert.ToDouble(Console.ReadLine());

            if (n % 2 == 0)
            {
                Console.WriteLine(n + 2);
            }
            else
            {
                Console.WriteLine(n + 1);
            }
        }
    }
}
