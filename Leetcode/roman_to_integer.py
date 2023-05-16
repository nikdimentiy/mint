# LeetCode task: solution -> https://leetcode.com/problems/roman-to-integer/


class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Converts a Roman numeral to an integer.

        :param s: A string representing a Roman numeral.
        :type s: str
        :return: The integer value of the Roman numeral.
        :rtype: int
        """
        # Create a dictionary to map symbols to values
        values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        # Initialize variables to keep track of previous symbol and result
        prev = None
        result = 0

        # Iterate through the string of symbols
        for symbol in s:
            # Get the value of the current symbol
            value = values[symbol]

            # If the previous symbol is not None and its value is less than the current symbol's value,
            # subtract its value from the current symbol's value and add the difference to the result
            if prev is not None and values[prev] < value:
                result += value - 2 * values[prev]
            # Otherwise, just add the value of the current symbol to the result
            else:
                result += value

            # Set the current symbol as the previous symbol for the next iteration
            prev = symbol

        return result


s = Solution()
result = s.romanToInt("XXVII")
print(result)  # Output: 27
