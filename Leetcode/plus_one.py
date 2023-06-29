# LeetCode task: solving -> https://leetcode.com/problems/plus-one/description/
# 😎 Preparation for coding interview 🎯

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        Increments a large integer represented by an array of digits by one.

        Args:
            digits (List[int]): The array of digits representing the large integer.

        Returns:
            List[int]: The resulting array of digits after incrementing the large integer by one.
        """
        carry = 1  # Initialize the carry to 1 since we're incrementing by one
        for i in range(len(digits) - 1, -1, -1):
            # Iterate over the digits array in reverse order (from least significant to most significant)

            digits[i] += carry  # Increment the current digit by the carry
            # Update the carry by dividing the current digit by 10
            carry = digits[i] // 10
            # Update the current digit by taking the modulo 10 of its value
            digits[i] %= 10

        if carry:
            # If carry is still 1, add an additional digit at the most significant position
            digits.insert(0, 1)

        return digits


digits = [1, 2, 3]
solution = Solution()
result = solution.plusOne(digits)
print(result)  # Output: [1, 2, 4]
