// LeetCode interview preparation task: solution -> https://leetcode.com/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150

using System;

public class Program
{
    public static int MajorityElement(int[] nums)
    {
        if (nums.Length == 0)
        {
            throw new ArgumentException("The input list cannot be empty.");
        }

        // Initialize the candidate element and its count
        int candidate = nums[0];
        int count = 1;

        // Loop through the rest of the list
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

        // Return the candidate element
        return candidate;
    }

    public static void Main(string[] args)
    {
        int[] nums = { 2, 2, 1, 1, 1, 2, 2 };
        int result = MajorityElement(nums);
        Console.WriteLine(result); // Output: 2
    }
}
