using System;

public class Program
{
    /// <summary>
    /// Finds the majority element in an array of integers. 
    /// A majority element is an element that appears more than n/2 times.
    /// Uses Boyer-Moore Voting Algorithm for O(n) time complexity.
    /// </summary>
    /// <param name="nums">An array of integers.</param>
    /// <returns>The majority element in the array.</returns>
    /// <exception cref="ArgumentException">Thrown when the input array is empty.</exception>
    public static int MajorityElement(int[] nums)
    {
        if (nums.Length == 0)
        {
            throw new ArgumentException("The input list cannot be empty.");
        }

        // Initialize the candidate element and its count
        int candidate = nums[0];
        int count = 1;

        // Loop through the rest of the list to find the candidate
        for (int i = 1; i < nums.Length; i++)
        {
            // If the current element is equal to the candidate, increment the count
            if (nums[i] == candidate)
            {
                count++;
            }
            // Otherwise, decrement the count
            else
            {
                count--;
            }

            // If the count becomes zero, update the candidate and reset the count
            if (count == 0)
            {
                candidate = nums[i];
                count = 1;
            }
        }

        // Return the candidate element as the majority element
        return candidate;
    }

    public static void Main(string[] args)
    {
        // Example input array
        int[] nums = { 2, 2, 1, 1, 1, 2, 2 };

        // Find and print the majority element
        int result = MajorityElement(nums);
        Console.WriteLine(result); // Output: 2
    }
}
