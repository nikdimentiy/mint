# LeetCode task: solving -> https://leetcode.com/problems/add-binary/
# 😁 Coding interview -> preparation ❤️

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Initialize a variable to store the binary sum
        result = ""
        # Initialize a variable to store the carry
        carry = 0

        # Initialize variables to traverse the binary numbers from right to left
        i = len(a) - 1
        j = len(b) - 1

        # Loop until both binary numbers have been fully traversed
        while i >= 0 or j >= 0:
            # If there are no more bits left in the first binary number, set the bit to 0
            a_bit = int(a[i]) if i >= 0 else 0
            # If there are no more bits left in the second binary number, set the bit to 0
            b_bit = int(b[j]) if j >= 0 else 0

            # Calculate the sum of the current bits and the carry
            total = a_bit + b_bit + carry

            # Append the least significant bit of the sum to the result
            result += str(total % 2)

            # Update the carry
            carry = total // 2

            # Move to the next bit
            i -= 1
            j -= 1

        # If there is still a carry remaining, append it to the result
        if carry:
            result += str(carry)

        # Reverse the result to get the correct binary sum
        result = result[::-1]

        # Return the binary sum
        return result


# Driver code
# Create an instance of the Solution class
solution = Solution()

# Test case 1
a = "11"
b = "1"
print(solution.addBinary(a, b))  # Output: "100"

# Test case 2
a = "1010"
b = "1011"
print(solution.addBinary(a, b))  # Output: "10101"
