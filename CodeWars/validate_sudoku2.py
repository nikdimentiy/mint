import math

class Sudoku(object):
    """
    A class to represent a Sudoku puzzle and validate its solution.

    Attributes:
    -----------
    board : list of list of int
        A 2D list representing the Sudoku board.

    Methods:
    --------
    is_valid():
        Checks if the Sudoku board is valid.
    """

    def __init__(self, board):
        """
        Constructs all the necessary attributes for the Sudoku object.

        Parameters:
        -----------
        board : list of list of int
            A 2D list representing the Sudoku board.
        """
        self.board = board

    def is_valid(self):
        """
        Checks if the Sudoku board is valid.

        Returns:
        --------
        bool
            True if the Sudoku board is valid, False otherwise.
        """
        # Check if the board is a list
        if not isinstance(self.board, list):
            return False

        n = len(self.board)
        rootN = int(round(math.sqrt(n)))

        # Check if the board size is a perfect square
        if rootN * rootN != n:
            return False

        # Helper function to check if a row is valid
        isValidRow = lambda r: (isinstance(r, list) and
                                len(r) == n and
                                all(map(lambda x: type(x) == int, r)))

        # Check if all rows are valid
        if not all(map(isValidRow, self.board)):
            return False

        # Set of numbers from 1 to n
        oneToN = set(range(1, n + 1))

        # Helper function to check if a list contains numbers from 1 to n
        isOneToN = lambda l: set(l) == oneToN

        # Transpose the board to check columns
        transpose = [[self.board[j][i] for i in range(n)] for j in range(n)]

        # Extract 3x3 squares
        squares = [[self.board[p + x][q + y] for x in range(rootN)
                                             for y in range(rootN)]
                                             for p in range(0, n, rootN)
                                             for q in range(0, n, rootN)]

        # Check if all rows, columns, and squares are valid
        return (all(map(isOneToN, self.board)) and
                all(map(isOneToN, transpose)) and
                all(map(isOneToN, squares)))

# Driver code to test the Sudoku class
if __name__ == "__main__":
    # Example of a valid 9x9 Sudoku board
    valid_board = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]

    # Example of an invalid 9x9 Sudoku board
    invalid_board = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 0]  # Invalid entry
    ]

    sudoku_valid = Sudoku(valid_board)
    sudoku_invalid = Sudoku(invalid_board)

    print("Valid Sudoku board:", sudoku_valid.is_valid())  # Should print: True
    print("Invalid Sudoku board:", sudoku_invalid.is_valid())  # Should print: False
