using System;

namespace Softcode
{
    /// <summary>
    /// This program calculates the roots of a quadratic equation given the coefficients a, b, and c.
    /// It then prints the roots to the console.
    /// </summary>
    class MainClass
    {
        public static void Main(string[] args)
        {
            Console.WriteLine("Give me the value of 'a' (coefficient of x^2): ");
            var a = Convert.ToDouble(Console.ReadLine());

            Console.WriteLine("Give me the value of 'b' (coefficient of x): ");
            var b = Convert.ToDouble(Console.ReadLine());

            Console.WriteLine("Give me the value of 'c' (constant term): ");
            var c = Convert.ToDouble(Console.ReadLine());

            // Calculate the discriminant
            var discriminant = Math.Pow(b, 2) - 4 * a * c;

            if (discriminant > 0)
            {
                // Calculate and display two distinct real roots
                var x1 = (-b - Math.Sqrt(discriminant)) / (2 * a);
                var x2 = (-b + Math.Sqrt(discriminant)) / (2 * a);

                // Print the roots in ascending order
                if (x1 > x2)
                {
                    Console.WriteLine("Roots are: ");
                    Console.WriteLine(x2);
                    Console.WriteLine(x1);
                }
                else
                {
                    Console.WriteLine("Roots are: ");
                    Console.WriteLine(x1);
                    Console.WriteLine(x2);
                }
            }
            else if (discriminant == 0)
            {
                // Calculate and display a single real root
                var x = -b / (2 * a);
                Console.WriteLine("Root is: ");
                Console.WriteLine(x);
            }
            else
            {
                // Display a message for complex roots
                Console.WriteLine("The equation has complex roots.");
            }
        }
    }
}
