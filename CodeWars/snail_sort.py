def snail(array):
    """
    Returns the elements of a 2D array in a clockwise spiral order.

    This function takes a 2D square array as input and returns its elements in a specific order:
    starting from the top-left corner, it traverses the outermost layer of the array in a clockwise
    spiral, then moves inward and repeats the process for the inner layers until all elements are
    collected.

    Parameters:
    ----------
    array : list of lists
        A 2D square array (list of lists) where each sublist represents a row.

    Returns:
    -------
    list
        A list containing the elements of the input array in clockwise spiral order.

    Example:
    --------
    >>> snail([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    [1, 2, 3, 6, 9, 8, 7, 4, 5]

    Explanation:
    ------------
    - The function starts at the top-left corner (1) and moves right: [1, 2, 3].
    - Then it moves down the rightmost column: [6, 9].
    - Next, it moves left along the bottom row: [8, 7].
    - Finally, it moves up the leftmost column: [4, 5].
    - The result is [1, 2, 3, 6, 9, 8, 7, 4, 5].
    """
    ret = []
    if array and array[0]:  # Ensure the array is not empty
        size = len(array)  # Determine the size of the square array
        for n in range((size + 1) // 2):  # Loop through each layer of the spiral
            # Traverse the top row from left to right
            for x in range(n, size - n):
                ret.append(array[n][x])
            # Traverse the right column from top to bottom
            for y in range(1 + n, size - n):
                ret.append(array[y][-1 - n])
            # Traverse the bottom row from right to left (if not already covered)
            for x in range(2 + n, size - n + 1):
                ret.append(array[-1 - n][-x])
            # Traverse the left column from bottom to top (if not already covered)
            for y in range(2 + n, size - n):
                ret.append(array[-y][n])
    return ret


# Driver Code
if __name__ == "__main__":
    # Example 1: 3x3 matrix
    print(snail([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]]))  # Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]

    # Example 2: 4x4 matrix
    print(snail([[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 10, 11, 12],
                 [13, 14, 15, 16]]))  # Output: [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]

    # Example 3: Empty matrix
    print(snail([]))  # Output: []

    # Example 4: Single-element matrix
    print(snail([[42]]))  # Output: [42]

    # Example 5: 2x2 matrix
    print(snail([[1, 2],
                 [3, 4]]))  # Output: [1, 2, 4, 3]
