/* The Insertion Sort Algorithm maintains two sub-lists named sorted sub-list and unsorted sub-list. 
Through each iteration, the sorted sub-list increased and the unsorted sub-list keeps on decreasing.*/

using System;

namespace Softcode
{
    public class Example
    {
        public static void Main(string[] args)
        {
            int[] arr = new int[5] { 8, 5, 7, 3, 1 };
            int n = 5, i, j, val;
            Console.WriteLine("Insertion Sort");
            Console.Write("Initial array is: ");
            for (i = 0; i < n; i++)
            {
                Console.Write(arr[i] + " ");
            }
            for (i = 1; i < n; i++)
            {
                val = arr[i];
                for (j = i - 1; j >= 0;)
                {
                    if (val < arr[j])
                    {
                        arr[j + 1] = arr[j];
                        j--;
                        arr[j + 1] = val;
                    }
                    else
                    {
                        break;
                    }   
                }
            }
            Console.Write("\nSorted Array is: ");
            for (i = 0; i < n; i++)
            {
                Console.Write(arr[i] + " ");
            }

            Console.ReadKey();
        }
    }
}
