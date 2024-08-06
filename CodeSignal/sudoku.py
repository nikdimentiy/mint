def solution(grid):
    """
    Check if a given 9x9 Sudoku grid is a valid solution.

    A valid Sudoku solution must satisfy the following conditions:
    1. Each row must contain the digits 1-9 without repetition.
    2. Each column must contain the digits 1-9 without repetition.
    3. Each of the nine 3x3 sub-grids must contain the digits 1-9 without repetition.

    Args:
        grid (list of list of int): A 9x9 list representing the Sudoku grid.

    Returns:
        bool: True if the grid is a valid Sudoku solution, False otherwise.
    """
    
    # Check each row for uniqueness of digits
    for row in grid:
        if len(set(row)) != 9 or any(num < 1 or num > 9 for num in row):
            return False

    # Check each column for uniqueness of digits
    for col in range(9):
        if len(set(grid[row][col] for row in range(9))) != 9:
            return False

    # Check each 3x3 sub-grid for uniqueness of digits
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid = [grid[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if len(set(subgrid)) != 9 or any(num < 1 or num > 9 for num in subgrid):
                return False

    # If all checks pass, then the grid is a correct solution to Sudoku
    return True

# Driver code to test the solution function
if __name__ == "__main__":
    # Example valid Sudoku grid
    valid_grid = [
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

    # Example invalid Sudoku grid
    invalid_grid = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]  # Duplicate '5' in the last row
    ]

    # Test the valid grid
    print("Valid grid test:", solution(valid_grid))  # Expected output: True

    # Test the invalid grid
    print("Invalid grid test:", solution(invalid_grid))  # Expected output: False
