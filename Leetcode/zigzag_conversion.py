# LeetCode task: solution -> https://leetcode.com/problems/zigzag-conversion/description/
# 🔥 Preparation to coding interview 😎

class Solution:
    """
    This class contains a method that converts a string into a zigzag pattern.
    """
    def convert(self, s: str, numRows: int) -> str:
        """
        This method takes in a string and an integer representing the number of rows to be used in the zigzag pattern.
        It returns the string in zigzag pattern.
        """
        if numRows == 1:
            return s
        rows = [''] * numRows
        direction = -1
        row = 0
        for c in s:
            rows[row] += c
            if row == 0 or row == numRows - 1:
                direction = -direction
            row += direction
        return ''.join(rows)

if __name__ == '__main__':
    """
    This is the driver code that creates an object of the Solution class and calls its convert method.
    """
    s = Solution()
    print(s.convert("PAYPALISHIRING", 3))

