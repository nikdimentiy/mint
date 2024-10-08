def createDict(keys, values):
    """
    Create a dictionary from two lists: keys and values.

    If the number of keys is greater than the number of values,
    None will be appended to the values list until both lists
    are of equal length.

    Parameters:
    keys (list): A list of keys for the dictionary.
    values (list): A list of values corresponding to the keys.

    Returns:
    dict: A dictionary mapping keys to values.
    """
    
    # Ensure that the values list is as long as the keys list
    while len(keys) > len(values):
        values.append(None)  # Append None to values if there are not enough values

    # Create a dictionary by zipping keys and values together
    dictionary = dict(zip(keys, values))
    return dictionary

# Driver code to test the createDict function
if __name__ == "__main__":
    # Example keys and values
    keys = ['a', 'b', 'c', 'd']
    values = [1, 2, 3]  # One less than the number of keys

    # Create the dictionary
    result_dict = createDict(keys, values)

    # Print the resulting dictionary
    print("Resulting Dictionary:", result_dict)
