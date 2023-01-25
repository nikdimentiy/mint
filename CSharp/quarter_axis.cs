// quarter axis (Coordinate System)
using System;

namespace Softcode
{
    class MainClass
    {
        public static void Main(string[] args)
        {
            Console.WriteLine("Give me first coordinates (x): ");
            double x = Convert.ToDouble(Console.ReadLine());

            Console.WriteLine("Give me second coordinates (y): ");
            double y = Convert.ToDouble(Console.ReadLine());

            if (x > 0 && y > 0)
            {
                Console.WriteLine(1);
            }

            if (x < 0 && y > 0)
            {
                Console.WriteLine(2);
            }

            if (x < 0 && y < 0)
            {
                Console.WriteLine(3);
            }

            if (x > 0 && y < 0)
            {
                Console.WriteLine(4);
            }
        }
    }
}
