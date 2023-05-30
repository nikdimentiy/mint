// LeetCode task: solution -> https://leetcode.com/problems/remove-element/description/

using System;
using System.Collections.Generic;

public class Solution
{
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
        Console.WriteLine("Modified nums1: " + string.Join(", ", nums1.GetRange(0, result1)));

        // Test case 2
        List<int> nums2 = new List<int> { 0, 1, 2, 2, 3, 0, 4, 2 };
        int val2 = 2;
        int result2 = solution.RemoveElement(nums2, val2);
        Console.WriteLine("Result 2: " + result2);  // Expected output: 5
        Console.WriteLine("Modified nums2: " + string.Join(", ", nums2.GetRange(0, result2)));
    }
}
