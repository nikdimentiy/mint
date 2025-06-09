def pyramid(n):
    """
    Generate a pyramid structure as a list of lists.

    Each inner list represents a level of the pyramid, 
    containing the number 1 repeated for the number of elements 
    equal to the level number.

    Parameters:
    n (int): The number of levels in the pyramid.

    Returns:
    list: A list of lists representing the pyramid.
    """
    # Create a list of lists where each inner list contains the number 1
    # repeated 'x' times, where 'x' is the current level (1 to n).
    return [[1] * x for x in range(1, n + 1)]

# Driver code to test the pyramid function
if __name__ == "__main__":
    # Define the number of levels for the pyramid
    levels = 5
    # Generate the pyramid
    result = pyramid(levels)
    # Print the result
    for level in result:
        print(level)
