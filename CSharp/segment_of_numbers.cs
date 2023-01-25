// the code calculate: product of numbers on the segment from a to b, ending in 7
using System;

namespace Softcode
{
    class MainClass
    {
        public static void Main(string[] args)
        {
            Console.WriteLine("Enter a first integer number: ");
            int a = Convert.ToInt32(Console.ReadLine());

            Console.WriteLine("Enter a second integer number: ");
            int b = Convert.ToInt32(Console.ReadLine());

            int productSegment = 1;
            for (int i = a; i <= b; i++)
            {
                if (i % 10 == 7)
                {
                    productSegment = productSegment * i;
                }
            }
            Console.WriteLine("The product of numbers on the segment from " 
                          + a + " to " + b + " ending in 7 is: " + productSegment);
        }
    }
}
