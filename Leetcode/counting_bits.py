# LeetCode task: Count the number of 1's in a binary representation -> # 338
# https://leetcode.com/problems/counting-bits/description/

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        Counts the number of 1's in the binary representation of numbers from 0 to n (inclusive).

        Args:
        - n (int): The non-negative integer up to which the count of 1's should be calculated.

        Returns:
        - List[int]: A list containing the count of 1's for each number from 0 to n.
        """

        # Initialize the result array with all zeros
        ans = [0] * (n + 1)

        for i in range(1, n + 1):
            # Use the fact that the number of set bits in i is the same as the
            # number of set bits in i/2 if i is even, or i/2 + 1 if i is odd.
            ans[i] = ans[i // 2] + (i % 2)

        return ans


# Example usage:
solution = Solution()

n1 = 2
print(solution.countBits(n1))  # Output: [0, 1, 1]

n2 = 5
print(solution.countBits(n2))  # Output: [0, 1, 1, 2, 1, 2]
