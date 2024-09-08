def colour_association(arr):
    """
    This function takes a 2D array where each element contains a color and its common association.
    It returns a list of dictionaries, where each dictionary has the color as the key and its 
    association as the value.

    Parameters:
    arr (list of list): A 2D array containing colors and their associations.

    Returns:
    list of dict: A list of dictionaries with colors as keys and associations as values.
    """
    # Create a list of dictionaries from the input array
    return [{i[0]: i[1]} for i in arr]

# Driver code to test the function
if __name__ == "__main__":
    # Sample input: a 2D array of colors and their associations
    color_associations = [
        ["Red", "Passion"],
        ["Blue", "Calm"],
        ["Green", "Nature"],
        ["Yellow", "Happiness"],
        ["Black", "Mystery"]
    ]

    # Call the function and store the result
    result = colour_association(color_associations)

    # Print the result
    print(result)
