using System;

public class Solution
{
    /// <summary>
    /// Calculates the maximum profit that can be achieved from buying and selling stock.
    /// The function assumes that you can only complete one transaction (i.e., buy one and sell one share of the stock).
    /// </summary>
    /// <param name="prices">An array of integers representing the stock prices on different days.</param>
    /// <returns>The maximum profit that can be achieved. If no profit can be made, returns 0.</returns>
    public int MaxProfit(int[] prices)
    {
        // Check if there are at least 2 prices in the array
        if (prices.Length < 2)
        {
            return 0; // Not enough prices to make a transaction
        }

        int minPrice = prices[0]; // Initialize the minimum price to the first day's price
        int maxProfit = 0; // Initialize the maximum profit to 0

        // Iterate over the prices array starting from the second price
        for (int i = 1; i < prices.Length; i++)
        {
            // Update the minimum price if a smaller price is encountered
            if (prices[i] < minPrice)
            {
                minPrice = prices[i];
            }
            else
            {
                // Calculate the potential profit if sold at the current price
                int profit = prices[i] - minPrice;
                // Update the maximum profit if the current profit is greater
                maxProfit = Math.Max(maxProfit, profit);
            }
        }

        return maxProfit; // Return the maximum profit found
    }
}

class Program
{
    static void Main(string[] args)
    {
        // Example stock prices for testing
        int[] prices = { 7, 1, 5, 3, 6, 4 };

        // Create an instance of the Solution class
        Solution solution = new Solution();

        // Call the MaxProfit method to calculate the maximum profit
        int maxProfit = solution.MaxProfit(prices);

        // Print the result
        Console.WriteLine("Maximum Profit: " + maxProfit);
    }
}
