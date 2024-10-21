class Solution:
    """
    This class provides a method to convert a given string into a zigzag pattern 
    based on a specified number of rows. The zigzag pattern is formed by writing 
    the characters of the string in a zigzag manner across the specified number 
    of rows and then reading the rows sequentially to form the final string.

    Attributes:
        None
    """

    def convert(self, s: str, numRows: int) -> str:
        """
        Converts the input string into a zigzag pattern based on the specified number of rows.

        Args:
            s (str): The input string to be converted.
            numRows (int): The number of rows to be used in the zigzag pattern.

        Returns:
            str: The string converted into a zigzag pattern.
        """
        # If there is only one row, return the original string
        if numRows == 1:
            return s
        
        # Create a list to hold the strings for each row
        rows = [''] * numRows
        direction = -1  # This will help in changing the direction of row traversal
        row = 0  # Start from the first row

        # Iterate through each character in the input string
        for c in s:
            rows[row] += c  # Add the character to the current row
            
            # Change direction when reaching the top or bottom row
            if row == 0 or row == numRows - 1:
                direction = -direction
            
            # Move to the next row in the current direction
            row += direction
        
        # Join all rows to form the final zigzag string
        return ''.join(rows)

if __name__ == '__main__':
    """
    Driver code to test the Solution class and its convert method.
    It creates an instance of the Solution class and calls the convert method 
    with a sample input, then prints the result.
    """
    s = Solution()
    # Test case: Convert the string "PAYPALISHIRING" into a zigzag pattern with 3 rows
    result = s.convert("PAYPALISHIRING", 3)
    print(result)  # Expected output: "PAHNAPLSIIGYIR"
