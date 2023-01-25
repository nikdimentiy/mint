// the code calculate: the arithmetic mean the elements of sequence

using System;

namespace Softcode
{
    class MainClass
    {
        public static void Main(string[] args)
        {
            Console.WriteLine("Enter integer number (make a sequence): ");
            Console.WriteLine("For the terminate input - please enter (zero)");
            int n = Convert.ToInt32(Console.ReadLine());

            double sum = 0;
            int count = 0;

            while (n != 0)
            {
                sum = sum + n;
                n = Convert.ToInt32(Console.ReadLine());
                count++;
            }
            
            double result = sum / count;
            Console.WriteLine();
            Console.Write("The arithmetic mean of elements of the sequence is: ");
            Console.WriteLine(result);
        }
    }
}

