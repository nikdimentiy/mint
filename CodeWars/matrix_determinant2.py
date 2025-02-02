import numpy as np

def determinant(a):
    """
    Calculate the determinant of a square matrix using NumPy.
    
    The determinant is a scalar value that provides important information about a square matrix:
    - For a 1x1 matrix |a|, the determinant is simply a
    - For a 2x2 matrix [[a, b], [c, d]], the determinant is ad - bc
    - For larger matrices, it's calculated using more complex methods
    
    Args:
        a (list of lists): A square matrix represented as a list of lists
            where each inner list is a row of the matrix
    
    Returns:
        int: The rounded determinant of the input matrix
    
    Examples:
        >>> determinant([[5]])
        5
        >>> determinant([[1, 2], [3, 4]])
        -2
        >>> determinant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        0
    """
    # Convert input to numpy matrix and calculate determinant
    det = np.linalg.det(np.matrix(a))
    
    # Round to handle floating point precision issues
    return round(det)

# Driver code
if __name__ == "__main__":
    # Test 1x1 matrix
    matrix_1x1 = [[5]]
    print(f"1x1 Matrix Determinant: {determinant(matrix_1x1)}")
    
    # Test 2x2 matrix
    matrix_2x2 = [
        [1, 2],
        [3, 4]
    ]
    print(f"2x2 Matrix Determinant: {determinant(matrix_2x2)}")
    
    # Test 3x3 matrix
    matrix_3x3 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(f"3x3 Matrix Determinant: {determinant(matrix_3x3)}")
    
    # Test with a matrix that has a larger determinant
    matrix_large_det = [
        [4, 6],
        [3, 8]
    ]
    print(f"Matrix [[4, 6], [3, 8]] Determinant: {determinant(matrix_large_det)}")
