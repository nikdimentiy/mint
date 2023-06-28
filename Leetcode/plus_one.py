# LeetCode task: solution -> https://leetcode.com/problems/plus-one/


from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1  # Initialize the carry variable to 1
        n = len(digits)  # Get the length of the input list 'digits'

        # Iterate over the list 'digits' in reverse order
        for i in range(n - 1, -1, -1):
            digits[i] += carry  # Add the carry to the current digit
            carry = digits[i] // 10  # Calculate the new carry value
            digits[i] %= 10  # Get the remainder after dividing by 10

        if carry:
            # If there is still a carry, insert it at the beginning of the list
            digits.insert(0, carry)

        return digits  # Return the modified 'digits' list


digits = [1, 2, 3]  # Input list of digits
solution = Solution()  # Create an instance of the Solution class
result = solution.plusOne(digits)  # Call the plusOne method on the instance
print(result)  # Output the result
# Output: [1, 2, 4]
