// the code represent: arithmetic progression
using System;

namespace Softcode
{
    class MainClass
    {
        public static void Main(string[] args)
        {
            Console.WriteLine("Enter the first member of the arithmetic progress: ");
            int a1 = Convert.ToInt32(Console.ReadLine());

            Console.WriteLine("Enter the difference of arithmetic progression: ");
            int progressDifference = Convert.ToInt32(Console.ReadLine());

            Console.WriteLine("Enter the required member of the progression: ");
            int n = Convert.ToInt32(Console.ReadLine());

            int result = a1 + progressDifference * (n - 1);


            Console.Write("The given member of the arithmetic progression is: ");
            Console.WriteLine(result);
        }
    }
}

