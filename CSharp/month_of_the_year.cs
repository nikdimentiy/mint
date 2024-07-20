using System;

namespace Softcode
{
    class MainClass
    {
        /// <summary>
        /// This program takes a number representing a month and outputs the corresponding season.
        /// </summary>
        public static void Main(string[] args)
        {
            Console.WriteLine("Enter your favorite month (number): ");
            int monthNumber = Convert.ToInt32(Console.ReadLine());

            // Divide the month number by 3 to group months into seasons
            int season = monthNumber / 3;

            // Use a switch statement to determine the season based on the grouped month
            switch (season)
            {
                case 0:
                case 4:
                    Console.WriteLine("Winter");
                    break;
                case 1:
                    Console.WriteLine("Spring");
                    break;
                case 2:
                    Console.WriteLine("Summer");
                    break;
                case 3:
                    Console.WriteLine("Fall");
                    break;
                default:
                    Console.WriteLine("Invalid month number entered.");
                    break;
            }
        }
    }
}
