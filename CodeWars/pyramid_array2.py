def pyramid(n):
    """
    Generate a pyramid structure as a list of lists.

    Each inner list contains the number 1, and the number of inner lists 
    corresponds to the input integer n. The i-th inner list contains i 
    occurrences of the number 1.

    Parameters:
    n (int): The height of the pyramid (number of rows).

    Returns:
    list: A list of lists representing the pyramid structure.
    """
    result = []  # Initialize an empty list to hold the pyramid rows
    for i in range(1, n + 1):
        result.append(i * [1])  # Append a list of 'i' ones to the result
    return result

# Driver code to test the pyramid function
if __name__ == "__main__":
    height = 5  # Define the height of the pyramid
    pyramid_structure = pyramid(height)  # Generate the pyramid
    for row in pyramid_structure:  # Print each row of the pyramid
        print(row)
