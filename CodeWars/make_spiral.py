def spiralize(size):
    """
    Create a spiral matrix of a given size.

    The function generates a square matrix of the specified size, 
    filling it with a spiral pattern of 1s and 0s. The outermost 
    layer of the matrix is filled with 1s, and the inner layers 
    alternate between 1s and 0s, creating a spiral effect.

    Parameters:
    size (int): The size of the matrix (must be a positive odd integer).

    Returns:
    list: A 2D list representing the spiral matrix.
    """
    
    # Initialize the matrix with 1s or 0s based on the size
    matrix = list(map(lambda x: list(map(lambda y: 1 if (
        int(size + 1) / 2) % 2 == 1 else 0, range(0, size))), range(0, size)))
    
    spiral = 1  # Start with 1 for the outer layer
    for i in range(0, int(size / 2)):
        for u in range(0, size - i * 2):
            # Fill the current layer of the spiral
            matrix[i][u + i] = spiral  # Top row
            matrix[u + i][i] = spiral  # Left column
            matrix[size - i - 1][u + i] = spiral  # Bottom row
            matrix[u + i][size - i - 1] = spiral  # Right column

            # Handle the case for even-sized matrices
            if size % 4 == 0:
                if i != int(size / 2) - 1:
                    matrix[i + 1][i] = 1 - spiral  # Fill the inner layer
            else:
                matrix[i + 1][i] = 1 - spiral  # Fill the inner layer
        spiral = 1 - spiral  # Alternate between 1 and 0 for the next layer
    
    return matrix

# Driver code to test the spiralize function
if __name__ == "__main__":
    size = 5  # Example size
    spiral_matrix = spiralize(size)
    
    # Print the resulting spiral matrix
    for row in spiral_matrix:
        print(' '.join(map(str, row)))
