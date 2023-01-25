// quadratic equation (discriminant)
using System;

namespace Softcode
{
    class MainClass
    {
        public static void Main(string[] args)
        {
            Console.WriteLine("Give me first real number (a): ");
            var a = Convert.ToDouble(Console.ReadLine());

            Console.WriteLine("Give me second real number (b): ");
            var b = Convert.ToDouble(Console.ReadLine());

            Console.WriteLine("Give me third real number (c): ");
            var c = Convert.ToDouble(Console.ReadLine());

            var discriminant = Math.Pow(b, 2) - 4 * a * c;
            if (discriminant > 0)
            {
                var x1 = (-b - Math.Sqrt(discriminant)) / (2 * a);
                var x2 = (-b + Math.Sqrt(discriminant)) / (2 * a);
                if (x1 > x2)
                {
                    Console.WriteLine(x2);
                    Console.WriteLine(x1);
                }
                else
                {
                    Console.WriteLine(x1);
                    Console.WriteLine(x2);
                }
            }
            else
            {
                if (discriminant == 0)
                {
                    var x2 = (-b + Math.Sqrt(discriminant)) / (2 * a);
                    Console.WriteLine(x2);
                }
            }
        }
    }
}
