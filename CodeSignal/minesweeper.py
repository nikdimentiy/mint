def solution(matrix):
    """
    Calculate the difference between each cell's value in the matrix and the sum of its neighbors.

    Args:
        matrix (list of list of int): A 2D list representing the matrix of integers.

    Returns:
        list of list of int: A new matrix where each cell contains the difference between the sum of its 
                             neighboring cells and its original value.
    """
    # Create a dictionary to map complex coordinates to their corresponding values in the matrix
    field = {(x + y * 1j): v
             for y, row in enumerate(matrix)
             for x, v in enumerate(row)}
    
    # Calculate the new matrix based on the sum of neighbors
    return [[sum(field.get(p + i + j, 0) for i in (-1, 0, 1) for j in (-1j, 0, 1j)) - v
             for x, v in enumerate(row)
             for p in [x + 1j * y]]
            for y, row in enumerate(matrix)]

# Driver code to test the solution function
if __name__ == "__main__":
    # Example matrix
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    # Call the solution function and print the result
    result = solution(matrix)
    print("Original Matrix:")
    for row in matrix:
        print(row)
    print("\nResulting Matrix:")
    for row in result:
        print(row)
