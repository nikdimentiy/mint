// this code - is a binary conversion (with cycle)
using System;

namespace Softcode
{
    class MainClass
    {
        public static void Main(string[] args)
        {
            Console.WriteLine("Enter integer number: ");
            int number = Convert.ToInt32(Console.ReadLine());

            string binValue = Convert.ToString(number, 2);
            Console.WriteLine(binValue);
        }
    }
}