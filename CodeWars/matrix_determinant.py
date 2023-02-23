# Write a function that accepts a square matrix (N x N 2D array) and returns the determinant of the matrix.

# How to take the determinant of a matrix -- it is simplest to start with the smallest cases:

# A 1x1 matrix |a| has determinant a.

# A 2x2 matrix [ [a, b], [c, d] ]

def determinant(matrix):
    """
    Computes the determinant of a square matrix.
    """
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    elif n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        det = 0
        for j in range(n):
            minor = [[matrix[i][k]
                      for k in range(n) if k != j] for i in range(1, n)]
            det += (-1) ** j * matrix[0][j] * determinant(minor)
        return det
