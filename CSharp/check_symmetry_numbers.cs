// check for symmetry numbers (4 digit number)
using System;

namespace Softcode
{
    class MainClass
    {
        public static void Main(string[] args)
        {
            Console.WriteLine("Enter a four-digit number: ");
            int fourDigitNumber = Convert.ToInt32(Console.ReadLine());

            int firsthalfOf4DigitNumber =  fourDigitNumber/ 100;
            int secondhalfOf4DigitNumber = (fourDigitNumber % 100);


            int a = firsthalfOf4DigitNumber / 10;

            int b = firsthalfOf4DigitNumber % 10;


            int c = secondhalfOf4DigitNumber / 10;

            int d = secondhalfOf4DigitNumber % 10;


            if (b == c && a == d)
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

