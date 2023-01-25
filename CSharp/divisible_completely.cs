// how many times entered number is divisible by 3 completely
using System;

namespace Softcode
{
    class MainClass
    {
        public static void Main(string[] args)
        {
            Console.WriteLine("Enter integer number: ");
            int a = Convert.ToInt32(Console.ReadLine());
            
            int cnt = 0;
            while (a % 3 == 0)
            {
                a = a / 3;
                cnt++;
            }
            Console.WriteLine(cnt);
        }
    }
}
