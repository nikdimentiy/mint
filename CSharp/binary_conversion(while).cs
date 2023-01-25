// this code - is a binary conversion (with cycle)
using System;

namespace Softcode
{
    class MainClass
    {
        public static void Main(string[] args)
        {
            Console.WriteLine("Enter integer number: ");
            int n = Convert.ToInt32(Console.ReadLine());
            
            // defining the invertedNumberInBits variable to get the number in bits and the count counter:
            
            int invertedNumberInBits = 0;
            int count = 0;
            
            // We get the number in bits by getting the remainder of the division by 2 (it is either 0 or 1),
            // but it will be inverted and immediately read the number of digits of the inverted number
            // in bits to display it later on the screen:
            
            while (n > 0)
            {
                invertedNumberInBits = invertedNumberInBits * 10 + n % 2;
                n /= 2;
                count++;
            }
            
            // We output the inverted number in bits, starting from the end to the console, when it is output,
            // it will turn over again, actually, we will get what we are looking for: */
            
            while (count > 0)
            {
                Console.Write(invertedNumberInBits % 10);
                invertedNumberInBits /= 10;
                count--;
            }
        }
    }
}
