def solution(rows):
    """
    This function takes a list of strings (rows) and returns the indices of the columns 
    that have the minimum number of dots ('.') when the rows are transposed.

    Args:
    rows (list of str): A list of strings representing rows of a grid.

    Returns:
    list of int: A list of indices of the columns with the minimum number of dots.
    """
    # Transpose the rows to get columns and count the number of dots in each column
    t = [''.join(r).lstrip('.').count('.') for r in zip(*rows)]
    
    # Find the minimum count of dots in the columns
    min_dots = min(t)
    
    # Return the indices of the columns that have the minimum count of dots
    return [i for i in range(len(t)) if t[i] == min_dots]

# Driver code
if __name__ == "__main__":
    # Example input
    rows = [
        "....",
        "...X",
        "..X.",
        ".X.."
    ]
    
    # Call the solution function and print the result
    result = solution(rows)
    print("Indices of columns with the minimum number of dots:", result)
