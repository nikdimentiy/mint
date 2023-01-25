// distance between points in the coordinate system

using System;

namespace MainClass
{
    class Hello
    {
        static void Main()
        {
            Console.WriteLine("Enter the coordinates of first point: ");

            Console.Write("X1 = ");
            double x1 = Convert.ToDouble(Console.ReadLine());
            Console.Write("Y1 = ");
            double y1 = Convert.ToDouble(Console.ReadLine());

            Console.WriteLine("Enter the coordinates of second point: ");
            Console.Write("X2 = ");
            double x2 = Convert.ToDouble(Console.ReadLine());
            Console.Write("Y2 = ");
            double y2 = Convert.ToDouble(Console.ReadLine());


            double horizontalDistance = Math.Pow(x2 - x1, 2);
            double verticalDistance = Math.Pow(y2 - y1, 2);

            double distance = Math.Sqrt(horizontalDistance + verticalDistance);

            Console.Write("Distance between the given points is: ");
            Console.WriteLine(distance);
        }
    }
}
