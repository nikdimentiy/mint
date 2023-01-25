// tiny code: power of number "2" (cycle "while")
using System;

namespace Softcode
{
    class MainClass
    {
        public static void Main(string[] args)
        {
            Console.WriteLine("Enter integer number: ");
            int n = Convert.ToInt32(Console.ReadLine());

            int power = 1;
            int degree = 0;

            while (degree < n)
            {
                power *= 2;
                degree++;
            }
            Console.WriteLine(power);
        }
    }
}
