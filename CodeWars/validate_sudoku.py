from math import sqrt

class Sudoku(object):
    """
    A class to validate Sudoku boards of any square size (4x4, 9x9, 16x16, etc.).
    
    The board must be a square grid where each row, column, and square block contains
    all numbers from 1 to n without repetition, where n is the size of the board.
    
    Attributes:
        board (list): 2D list representing the Sudoku board
        n (int): Size of the board (9 for standard Sudoku)
        sqrt_user (int): Square root of n (3 for standard Sudoku)
    """
    
    def __init__(self, board):
        """
        Initialize the Sudoku board validator.
        
        Args:
            board (list): 2D list representing the Sudoku board
        """
        self.board = board
        self.n = len(self.board)
        self.sqrt_user = int(sqrt(self.n))
        
    def is_valid(self):
        """
        Check if the Sudoku board is valid.
        
        Returns:
            bool: True if the board is valid, False otherwise
        """
        # Check size and contents of each row
        for row in self.board:
            if len(row) != self.n:
                return False
            for n in row:
                # Make sure every entry is an integer and is in valid range
                if not isinstance(n, int) or not self.in_range(n):
                    return False
                    
        # Check rows and columns
        for n in range(self.n):
            if not self.valid_row(n) or not self.valid_col(n):
                return False
                
        # Check square blocks
        for i in range(self.sqrt_user):
            for j in range(self.sqrt_user):
                if not self.valid_square(i, j):
                    return False
        return True
        
    def in_range(self, n):
        """
        Check if a number is in valid range (1 to n).
        
        Args:
            n (int): Number to check
            
        Returns:
            bool: True if number is in range, False otherwise
        """
        return n >= 1 and n <= self.n
        
    def valid_row(self, i):
        """
        Check if a row contains all numbers from 1 to n exactly once.
        
        Args:
            i (int): Row index to check
            
        Returns:
            bool: True if row is valid, False otherwise
        """
        valid = [False] * self.n
        row = self.board[i]
        for n in row:
            try:
                valid[n - 1] = True
            except IndexError:
                return False
        return all(valid)
        
    def valid_col(self, j):
        """
        Check if a column contains all numbers from 1 to n exactly once.
        
        Args:
            j (int): Column index to check
            
        Returns:
            bool: True if column is valid, False otherwise
        """
        valid = [False] * self.n
        col = [row[j] for row in self.board]
        for n in col:
            try:
                valid[n - 1] = True
            except IndexError:
                return False
        return all(valid)
        
    def valid_square(self, ni, nj):
        """
        Check if a square block contains all numbers from 1 to n exactly once.
        
        Args:
            ni (int): Row index of the square block
            nj (int): Column index of the square block
            
        Returns:
            bool: True if square block is valid, False otherwise
        """
        # Calculate starting indices for the square block
        ni *= self.sqrt_user
        nj *= self.sqrt_user
        valid = [False] * self.n
        # Check each cell in the square block
        for i in range(ni, ni + self.sqrt_user):
            for j in range(nj, nj + self.sqrt_user):
                n = self.board[i][j]
                try:
                    valid[n - 1] = True
                except IndexError:
                    return False
        return all(valid)

# Driver code
if __name__ == "__main__":
    # Valid 9x9 Sudoku board
    valid_board = [
        [5,3,4,6,7,8,9,1,2],
        [6,7,2,1,9,5,3,4,8],
        [1,9,8,3,4,2,5,6,7],
        [8,5,9,7,6,1,4,2,3],
        [4,2,6,8,5,3,7,9,1],
        [7,1,3,9,2,4,8,5,6],
        [9,6,1,5,3,7,2,8,4],
        [2,8,7,4,1,9,6,3,5],
        [3,4,5,2,8,6,1,7,9]
    ]
    
    # Invalid 9x9 Sudoku board (duplicate numbers in first row)
    invalid_board = [
        [5,3,4,6,7,8,9,1,1],  # Note the duplicate 1
        [6,7,2,1,9,5,3,4,8],
        [1,9,8,3,4,2,5,6,7],
        [8,5,9,7,6,1,4,2,3],
        [4,2,6,8,5,3,7,9,1],
        [7,1,3,9,2,4,8,5,6],
        [9,6,1,5,3,7,2,8,4],
        [2,8,7,4,1,9,6,3,5],
        [3,4,5,2,8,6,1,7,9]
    ]
    
    # Test valid board
    sudoku = Sudoku(valid_board)
    print("Valid board test:", sudoku.is_valid())  # Should print: True
    
    # Test invalid board
    sudoku = Sudoku(invalid_board)
    print("Invalid board test:", sudoku.is_valid())  # Should print: False
    
    # Test 4x4 valid board
    small_valid_board = [
        [1,2,3,4],
        [3,4,1,2],
        [2,1,4,3],
        [4,3,2,1]
    ]
    sudoku = Sudoku(small_valid_board)
    print("4x4 valid board test:", sudoku.is_valid())  # Should print: True
