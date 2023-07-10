# LeetCode task: solution -> https://leetcode.com/problems/generate-parentheses/description/
# 🤞 Preparation for coding interview 🎯


from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """Generate all possible valid combinations of n pairs of parentheses.

        Args:
            n (int): The number of pairs of parentheses.

        Returns:
            List[str]: A list of strings, each containing a valid combination of parentheses.
        """
        result = []  # Initialize an empty list to store the results
        # Call the backtrack helper function with an empty string and zero counts
        self.backtrack(result, '', 0, 0, n)
        return result  # Return the final list of results

    def backtrack(self, result, current, open_count, close_count, n):
        """Helper function to recursively generate valid combinations of parentheses using backtracking.

        Args:
            result (List[str]): The list of results to be updated.
            current (str): The current string being built.
            open_count (int): The number of open parentheses in the current string.
            close_count (int): The number of close parentheses in the current string.
            n (int): The number of pairs of parentheses.
        """
        if len(current) == 2 * n:  # Base case: if the current string has reached the maximum length
            result.append(current)  # Add the current string to the result list
            return  # Return from the recursion

        if open_count < n:  # If we can still add more open parentheses
            # Add an open parenthesis and recurse
            self.backtrack(result, current +
                           '(', open_count + 1, close_count, n)

        if close_count < open_count:  # If we can still add more close parentheses
            # Add a close parenthesis and recurse
            self.backtrack(result, current + ')',
                           open_count, close_count + 1, n)


# Driver code
n = 3  # Set the number of pairs of parentheses
solution = Solution()  # Create an instance of the Solution class
# Call the generateParenthesis method with n as the argument
output = solution.generateParenthesis(n)
print(output)  # Print the output list
