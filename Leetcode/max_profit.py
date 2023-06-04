# LeetCode task: solution -> https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/?envType=study-plan-v2&envId=top-interview-150
# 🎯 150 task preparation to the interview 😎

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Calculates the maximum profit that can be achieved by buying and selling a stock.

        Args:
            prices (List[int]): The list of stock prices.

        Returns:
            int: The maximum profit that can be achieved.

        """

        # Check if there are at least 2 prices in the list
        if len(prices) < 2:
            return 0

        # Initialize variables
        min_price = prices[0]  # Track the minimum price seen so far
        max_profit = 0  # Track the maximum profit seen so far

        # Iterate over the prices list
        for i in range(1, len(prices)):
            if prices[i] < min_price:
                # Update the minimum price if a smaller price is encountered
                min_price = prices[i]
            else:
                # Calculate the potential profit if sold at the current price
                profit = prices[i] - min_price
                # Update the maximum profit if necessary
                max_profit = max(max_profit, profit)

        return max_profit


prices = [7, 1, 5, 3, 6, 4]

# Create an instance of the Solution class
solution = Solution()

# Call the maxProfit method to calculate the maximum profit
max_profit = solution.maxProfit(prices)

# Print the result
print("Maximum Profit:", max_profit)
