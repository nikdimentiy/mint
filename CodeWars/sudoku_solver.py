import copy  
import math  
from typing import List, Tuple  

Sudoku = List[List[int]]  

class SudokuError(Exception):  
    """Exception raised when unable to solve the Sudoku puzzle."""  
    pass  

def sudoku_solved(puzzle: Sudoku) -> bool:  
    """  
    Check if the Sudoku puzzle is solved.  

    A Sudoku puzzle is considered solved if all cells are filled.  

    Args:  
        puzzle (Sudoku): A 2D list representing the Sudoku puzzle.  

    Returns:  
        bool: True if the puzzle is solved, False otherwise.  
    """  
    return all(all(row) for row in puzzle)  

def get_row(puzzle: Sudoku, i: int) -> List[int]:  
    """  
    Get the specified row from the Sudoku puzzle.  

    Args:  
        puzzle (Sudoku): A 2D list representing the Sudoku puzzle.  
        i (int): The index of the row to retrieve.  

    Returns:  
        List[int]: The specified row as a list of integers.  
    """  
    return puzzle[i]  

def get_column(puzzle: Sudoku, i: int) -> List[int]:  
    """  
    Get the specified column from the Sudoku puzzle.  

    Args:  
        puzzle (Sudoku): A 2D list representing the Sudoku puzzle.  
        i (int): The index of the column to retrieve.  

    Returns:  
        List[int]: The specified column as a list of integers.  
    """  
    return [row[i] for row in puzzle]  

def get_square(puzzle: Sudoku, i: int) -> List[int]:  
    """  
    Get the specified square (sub-grid) from the Sudoku puzzle.  

    Args:  
        puzzle (Sudoku): A 2D list representing the Sudoku puzzle.  
        i (int): The index of the square to retrieve.  

    Returns:  
        List[int]: The specified square as a list of integers.  
    """  
    size = len(puzzle)  
    little_square_size = int(math.sqrt(size))  

    x, y = divmod(i, little_square_size)  
    square = []  

    for row in puzzle[x * little_square_size: (x + 1) * little_square_size]:  
        square.extend(  
            row[y * little_square_size: (y + 1) * little_square_size]  
        )  

    return square  

# Driver code to test the functions  
if __name__ == "__main__":  
    # Example Sudoku puzzle (0 represents empty cells)  
    sudoku_puzzle = [  
        [5, 3, 0, 0, 7, 0, 0, 0, 0],  
        [6, 0, 0, 1, 9, 5, 0, 0, 0],  
        [0, 9, 8, 0, 0, 0, 0, 6, 0],  
        [8, 0, 0, 0, 6, 0, 0, 0, 3],  
        [4, 0, 0, 8, 0, 3, 0, 0, 1],  
        [7, 0, 0, 0, 2, 0, 0, 0, 6],  
        [0, 6, 0, 0, 0, 0, 2, 8, 0],  
        [0, 0, 0, 4, 1, 9, 0, 0, 5],  
        [0, 0, 0, 0, 8, 0, 0, 7, 9],  
    ]  

    # Check if the puzzle is solved  
    print("Is the Sudoku puzzle solved?", sudoku_solved(sudoku_puzzle))  

    # Get and print a specific row  
    row_index = 0  
    print(f"Row {row_index}:", get_row(sudoku_puzzle, row_index))  

    # Get and print a specific column  
    column_index = 1  
    print(f"Column {column_index}:", get_column(sudoku_puzzle, column_index))  

    # Get and print a specific square (sub-grid)  
    square_index = 0  
    print(f"Square {square_index}:", get_square(sudoku_puzzle, square_index))
