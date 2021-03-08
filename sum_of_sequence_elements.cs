// tiny code - defines the sum of a sequence: 
// in which the numbers are multiples of 2, but not multiples of 3

using System;

namespace Softcode
{
    class MainClass
    {
        public static void Main(string[] args)
        {
            Console.WriteLine("Enter integer number: ");
            int n = Convert.ToInt32(Console.ReadLine());

            int sum = 0;

            while (n != 0)
            {
                if (n % 2 == 0 && n % 3 != 0)
                    sum = sum + n;
                n = Convert.ToInt32(Console.ReadLine());
            }
            Console.WriteLine();
            Console.Write("The sum of entered numbers, that meet the condition is: ");
            Console.WriteLine(sum);
        }
    }
}


