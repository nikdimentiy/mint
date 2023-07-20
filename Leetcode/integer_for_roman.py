# LeetCode task: solution -> https://leetcode.com/problems/integer-to-roman/description/
# Preparation for coding interview


class Solution:
    def intToRoman(self, num: int) -> str:
        # Initialize lists for Roman numeral symbols and their equivalent values
        symbols = [
            "M",
            "CM",
            "D",
            "CD",
            "C",
            "XC",
            "L",
            "XL",
            "X",
            "IX",
            "V",
            "IV",
            "I",
        ]
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        # Initialize result string and index counter
        result = ""
        i = 0

        # Convert integer to Roman numeral symbols
        while num > 0:
            while num >= values[i]:
                result += symbols[i]  # Append the Roman numeral symbol
                num -= values[i]  # Subtract the current value from the input integer
            i += 1  # Increment the index counter

        # Return the Roman numeral representation of the input integer
        return result


# Test cases
solution = Solution()
print(solution.intToRoman(3))  # Output: "III"
print(solution.intToRoman(58))  # Output: "LVIII"
print(solution.intToRoman(1994))  # Output: "MCMXCIV"
