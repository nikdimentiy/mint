/**
 * @file Solution.cs
 * @brief Provides a solution to the LeetCode problem "Remove Element".
 *
 * This program defines a solution to the problem where elements equal to a given value 
 * are removed from a list, and the remaining elements are moved to the beginning of the list.
 * The method returns the number of elements that are not equal to the given value.
 */

using System;
using System.Collections.Generic;

public class Solution
{
    /**
     * Removes all instances of 'val' from the list 'nums' and returns the new length of the list.
     * 
     * @param nums A list of integers.
     * @param val The value to be removed from the list.
     * @return The number of elements in the list after removing 'val'.
     */
    public int RemoveElement(List<int> nums, int val)
    {
        // Initialize a pointer 'i' to keep track of the elements that are not equal to 'val'
        int i = 0;

        // Iterate through the 'nums' list using pointer 'j'
        for (int j = 0; j < nums.Count; j++)
        {
            // If the current element is not equal to 'val'
            if (nums[j] != val)
            {
                // Move the element to the 'i'th position and increment 'i'
                nums[i] = nums[j];
                i++;
            }
        }

        // Return the value of 'i' which represents the number of elements that are not equal to 'val'
        return i;
    }
}

public class Program
{
    public static void Main()
    {
        Solution solution = new Solution();

        // Test case 1
        List<int> nums1 = new List<int> { 3, 2, 2, 3 };
        int val1 = 3;
        int result1 = solution.RemoveElement(nums1, val1);
        Console.WriteLine("Result 1: " + result1);  // Expected output: 2
        Console.WriteLine("Modified nums1: " + string.Join(", ", nums1.GetRange(0, result1))); // Should print first 2 elements

        // Test case 2
        List<int> nums2 = new List<int> { 0, 1, 2, 2, 3, 0, 4, 2 };
        int val2 = 2;
        int result2 = solution.RemoveElement(nums2, val2);
        Console.WriteLine("Result 2: " + result2);  // Expected output: 5
        Console.WriteLine("Modified nums2: " + string.Join(", ", nums2.GetRange(0, result2))); // Should print first 5 elements
    }
}
