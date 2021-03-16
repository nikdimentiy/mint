// check for the existence of a triangle
using System;

namespace Softcode
{
    class MainClass
    {
        public static void Main(string[] args)
        {
            Console.WriteLine("Enter the first side of the triangle: ");
            int a = Convert.ToInt32(Console.ReadLine());

            Console.WriteLine("Enter the second side of the triangle: ");
            int b = Convert.ToInt32(Console.ReadLine());

            Console.WriteLine("Enter the third side of the triangle: ");
            int c = Convert.ToInt32(Console.ReadLine());


            if ((a < (b + c)) && (b < (a + c)) && (c < (a + b))) // basic conditions for a triangle
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

