// counting the sum of digits

using System;

namespace Softcode
{
    class MainClass
    {
        public static void Main(string[] args)
        {
            Console.WriteLine("Enter integer number: ");
            int n = Convert.ToInt32(Console.ReadLine());

            int sum = 0; // adder
            while (n > 0) // until the digits of the number run out
            {
                int digit = n % 10; // the last digit of the number
                sum = sum + digit; // add it to the adder
                n = n / 10; // getting rid of the last digit
            }

            Console.WriteLine(sum);
        }
    }
}

