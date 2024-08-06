def solution(matrix, width, center, t):
    """
    Rotates the elements of a square submatrix around a given center point.

    Parameters:
    matrix (list of list of int): The 2D matrix to be modified.
    width (int): The width of the square submatrix to rotate.
    center (tuple): A tuple (r, c) representing the center of the submatrix.
    t (int): The number of times to rotate the elements (in 90-degree increments).

    Returns:
    list of list of int: The modified matrix after rotation.
    """
    
    # Extract the row and column indices from the center
    [r, c] = center
    
    # Define the offsets for the elements in the square submatrix
    offset = [(-1, -1), (-1, 0), (-1, 1), (0, 1),
              (1, 1), (1, 0), (1, -1), (0, -1)]
    
    # Iterate over the layers of the square submatrix
    for d in range(1, width // 2 + 1):
        # Collect the values from the current layer
        v = [matrix[r + d * i][c + d * j] for (i, j) in offset]
        
        # Rotate the values based on the number of 90-degree turns (t)
        v = v[-(t % 8):] + v[:-(t % 8)]
        
        # Place the rotated values back into the matrix
        for o, (i, j) in enumerate(offset):
            matrix[r + d * i][c + d * j] = v[o]

    return matrix

# Driver code to test the solution function
if __name__ == "__main__":
    # Example matrix
    matrix = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]
    ]
    
    # Parameters for the rotation
    width = 3  # Width of the square submatrix
    center = (2, 2)  # Center of the submatrix (row, column)
    t = 1  # Number of 90-degree rotations

    # Print the original matrix
    print("Original Matrix:")
    for row in matrix:
        print(row)

    # Call the solution function
    modified_matrix = solution(matrix, width, center, t)

    # Print the modified matrix
    print("\nModified Matrix after rotation:")
    for row in modified_matrix:
        print(row)
