import itertools

def solution(size, nonogramField):
    """
    Check if the given nonogram field satisfies the specified row and column constraints.

    Args:
        size (int): The size of the nonogram (number of rows and columns).
        nonogramField (list of str): A list of strings representing the nonogram field,
                                      where '#' represents a filled cell and '.' represents an empty cell.

    Returns:
        bool: True if the nonogram field satisfies the constraints, False otherwise.
    """
    # Calculate the width for the constraints (half the size, rounded up)
    w = (size + 1) // 2
    
    # Check each row and each column for the constraints
    return all(
        # Compare the constraints for each row and column
        [int(s) for s in row[:w] if s.isdigit()] ==  # Extract the expected counts from the row
        [len(list(x)) for k, x in itertools.groupby(row) if k == '#']  # Count the filled cells
        for row in nonogramField + list(zip(*nonogramField))  # Check both rows and columns
    )

# Driver code to test the solution function
if __name__ == "__main__":
    # Example nonogram field
    nonogramField = [
        "##..",
        "#...",
        "##..",
        "...."
    ]
    
    size = len(nonogramField)  # Size of the nonogram (number of rows/columns)
    
    # Call the solution function and print the result
    result = solution(size, nonogramField)
    print("Does the nonogram field satisfy the constraints?", result)
