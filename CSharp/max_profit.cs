// LeetCode task: solution -> https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/?envType=study-plan-v2&envId=top-interview-150
// 150 task for interview preparation 🎯

using System;

public class Solution
{
    public int MaxProfit(int[] prices)
    {
        // Check if there are at least 2 prices in the array
        if (prices.Length < 2)
        {
            return 0;
        }

        int minPrice = prices[0]; // Track the minimum price seen so far
        int maxProfit = 0; // Track the maximum profit seen so far

        // Iterate over the prices array
        for (int i = 1; i < prices.Length; i++)
        {
            if (prices[i] < minPrice)
            {
                // Update the minimum price if a smaller price is encountered
                minPrice = prices[i];
            }
            else
            {
                // Calculate the potential profit if sold at the current price
                int profit = prices[i] - minPrice;
                // Update the maximum profit if necessary
                maxProfit = Math.Max(maxProfit, profit);
            }
        }

        return maxProfit;
    }
}

class Program
{
    static void Main(string[] args)
    {
        int[] prices = { 7, 1, 5, 3, 6, 4 };

        // Create an instance of the Solution class
        Solution solution = new Solution();

        // Call the MaxProfit method to calculate the maximum profit
        int maxProfit = solution.MaxProfit(prices);

        // Print the result
        Console.WriteLine("Maximum Profit: " + maxProfit);
    }
}
