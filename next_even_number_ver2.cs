// the tiny code represent - the next even number of entered number
using System;

namespace Softcode
{
    class MainClass
    {
        public static void Main(string[] args)
        {
            Console.WriteLine("Enter your number: ");

            int n = Convert.ToInt32(Console.ReadLine());
            Console.Write(n + 2 - n % 2);
        }
    }
}
