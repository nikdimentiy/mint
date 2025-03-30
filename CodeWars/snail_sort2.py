import numpy as np

def snail(array):
    """
    This function takes a 2D array (list of lists or numpy array) and returns 
    its elements in a "snail" order. The "snail" order starts from the top-left 
    corner, moves right across the first row, then spirals inward in a clockwise 
    manner until all elements are traversed.

    Parameters:
    array (list of lists or numpy.ndarray): A 2D array to be traversed in snail order.

    Returns:
    list: A list containing the elements of the input array in snail order.

    Example:
    >>> snail([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    [1, 2, 3, 6, 9, 8, 7, 4, 5]
    """
    # Initialize an empty list to store the snail traversal result
    m = []

    # Convert the input array to a numpy array for easier manipulation
    array = np.array(array)

    # Continue processing until the array is empty
    while len(array) > 0:
        # Add the first row of the array to the result list
        m += array[0].tolist()

        # Remove the first row and rotate the remaining array counter-clockwise
        # This effectively prepares the array for the next spiral layer
        array = np.rot90(array[1:])

    # Return the final snail-ordered list
    return m


# Driver code to test the function
if __name__ == "__main__":
    # Example 1: A 3x3 matrix
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("Input Matrix:")
    for row in matrix1:
        print(row)
    print("\nSnail Order Traversal:")
    print(snail(matrix1))

    # Example 2: A 4x4 matrix
    matrix2 = [
        [1,  2,  3,  4],
        [5,  6,  7,  8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    print("\nInput Matrix:")
    for row in matrix2:
        print(row)
    print("\nSnail Order Traversal:")
    print(snail(matrix2))

    # Example 3: A 2x2 matrix
    matrix3 = [
        [1, 2],
        [3, 4]
    ]
    print("\nInput Matrix:")
    for row in matrix3:
        print(row)
    print("\nSnail Order Traversal:")
    print(snail(matrix3))
