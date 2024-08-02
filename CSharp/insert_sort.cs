using System;

namespace Softcode
{
    /// <summary>
    /// This class demonstrates the Insertion Sort algorithm.
    /// The algorithm maintains two sub-lists: a sorted sub-list and an unsorted sub-list.
    /// In each iteration, the sorted sub-list increases in size while the unsorted sub-list decreases.
    /// </summary>
    public class Example
    {
        /// <summary>
        /// The main entry point for the program.
        /// It initializes an array, performs insertion sort on it, and displays the sorted array.
        /// </summary>
        /// <param name="args">Command line arguments (not used).</param>
        public static void Main(string[] args)
        {
            // Initialize an array of integers to be sorted
            int[] arr = new int[5] { 8, 5, 7, 3, 1 };
            int n = 5; // Size of the array
            int i, j, val; // Loop variables

            // Display the initial unsorted array
            Console.WriteLine("Insertion Sort");
            Console.Write("Initial array is: ");
            for (i = 0; i < n; i++)
            {
                Console.Write(arr[i] + " ");
            }

            // Perform Insertion Sort
            for (i = 1; i < n; i++)
            {
                val = arr[i]; // The current value to be inserted into the sorted sub-list
                // Start from the end of the sorted sub-list
                for (j = i - 1; j >= 0;)
                {
                    // If the current value is less than the element in the sorted sub-list
                    if (val < arr[j])
                    {
                        arr[j + 1] = arr[j]; // Shift the element to the right
                        j--; // Move to the next element in the sorted sub-list
                        arr[j + 1] = val; // Insert the current value at the correct position
                    }
                    else
                    {
                        break; // Break the loop if the correct position is found
                    }   
                }
            }

            // Display the sorted array
            Console.Write("\nSorted Array is: ");
            for (i = 0; i < n; i++)
            {
                Console.Write(arr[i] + " ");
            }

            // Wait for a key press before closing the console window
            Console.ReadKey();
        }
    }
}
