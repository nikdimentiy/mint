// quarter axis (Coordinate System)

using System;

namespace Softcode 
{
    class MainClass
    {
        public static void Main(string[] args)
        {
            double x = Convert.ToDouble(Console.ReadLine());
            double y = Convert.ToDouble(Console.ReadLine());
            if (x > 0)
                if (y > 0) Console.Write(1);
                else Console.Write(4);
            else
                if (y > 0) Console.Write(2);
            else Console.Write(3);
        }
    }
}