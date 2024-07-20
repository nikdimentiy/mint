using System;

namespace Prime
{
    class MainClass
    {
        /// <summary>
        /// This program checks if a lottery ticket number is lucky by comparing the sum of the first half and the second half of the number.
        /// </summary>
        public static void Main(string[] args)
        {
            Console.WriteLine("Enter your lottery ticket number: ");
            int six_digits_number = Convert.ToInt32(Console.ReadLine());

            // Split the lottery ticket number into equal halves of 3 characters (numbers)
            int first_half = (six_digits_number / 1000);
            int second_half = (six_digits_number % 1000);

            // Calculate the sum of the numbers in the first half 
            int s1 = first_half / 100;
            int x1 = (first_half % 100);
            int d1 = x1 / 10;
            int e1 = x1 % 10;
            int sum_first_half = (s1 + d1 + e1);

            // Calculate the sum of the second half
            int s2 = second_half / 100;
            int x2 = (second_half % 100);
            int d2 = x2 / 10;
            int e2 = x2 % 10;
            int sum_second_half = (s2 + d2 + e2);

            // Compare the sums of equal halves of the lottery ticket
            if (sum_first_half == sum_second_half)
            {
                Console.WriteLine("You have a lucky ticket!");
            }
            else
            {
                Console.WriteLine("Sorry! But try again - don't worry!");
            }
        }
    }
}
