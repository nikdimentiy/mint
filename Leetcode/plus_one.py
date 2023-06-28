# LeetCode task: solution -> https://leetcode.com/problems/plus-one/


from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        n = len(digits)

        for i in range(n - 1, -1, -1):
            digits[i] += carry
            carry = digits[i] // 10
            digits[i] %= 10

        if carry:
            digits.insert(0, carry)

        return digits


digits = [1, 2, 3]
solution = Solution()
result = solution.plusOne(digits)
print(result)  # Output: [1, 2, 4]
