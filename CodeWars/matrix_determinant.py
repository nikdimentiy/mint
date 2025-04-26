def determinant(matrix):
    """
    Computes the determinant of a square matrix using recursive expansion by minors.
    
    Args:
        matrix (list of list of numbers): A square matrix represented as a 2D list.
        
    Returns:
        number: The determinant of the matrix.
    
    The function works by:
        - Handling the base case of a 1x1 matrix.
        - Computing the determinant for a 2x2 matrix using the formula:
              ad - bc.
        - For larger matrices, recursively expanding along the first row.
    
    Example:
        >>> matrix = [
        ...    [1, 2, 3],
        ...    [0, 4, 5],
        ...    [1, 0, 6]
        ... ]
        >>> print(determinant(matrix))
        22
    """
    n = len(matrix)
    
    # Base case for 1x1 matrix
    if n == 1:
        return matrix[0][0]
    
    # Base case for 2x2 matrix
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    # Recursive case for NxN matrix
    det = 0
    # Loop through each element in the first row
    for j in range(n):
        # Create a minor matrix by excluding the first row and the current column j
        minor = [
            [matrix[i][k] for k in range(n) if k != j]
            for i in range(1, n)
        ]
        # Recursively compute the determinant using expansion of minors
        sign = (-1) ** j  # sign alternates based on column index
        det += sign * matrix[0][j] * determinant(minor)
    
    return det

# Driver code to test the determinant function
if __name__ == '__main__':
    # Test case 1: 1x1 matrix
    matrix_1x1 = [[5]]
    print("Determinant of 1x1 matrix:", determinant(matrix_1x1))  # Expected output: 5

    # Test case 2: 2x2 matrix
    matrix_2x2 = [
        [1, 2],
        [3, 4]
    ]
    # Expected output: (1*4) - (2*3) = 4 - 6 = -2
    print("Determinant of 2x2 matrix:", determinant(matrix_2x2))

    # Test case 3: 3x3 matrix
    matrix_3x3 = [
        [1, 2, 3],
        [0, 4, 5],
        [1, 0, 6]
    ]
    # Expected output calculation:
    # 1*(4*6 - 5*0) - 2*(0*6 - 5*1) + 3*(0*0 - 4*1) = 24 + 10 - 12 = 22
    print("Determinant of 3x3 matrix:", determinant(matrix_3x3))

    # Test case 4: 4x4 matrix
    matrix_4x4 = [
        [3, 2, 0, 1],
        [4, 0, 1, 2],
        [3, 0, 2, 1],
        [9, 2, 3, 1]
    ]
    print("Determinant of 4x4 matrix:", determinant(matrix_4x4))
