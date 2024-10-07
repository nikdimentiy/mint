def createDict(keys, values):
    """
    Create a dictionary from two lists: keys and values.

    Parameters:
    keys (list): A list of keys for the dictionary.
    values (list): A list of values corresponding to the keys.

    Returns:
    dict: A dictionary mapping each key to its corresponding value.
          If there are more keys than values, the remaining keys will be mapped to None.
    """
    d = {}  # Initialize an empty dictionary
    for e, i in enumerate(keys):
        if e < len(values):
            d[i] = values[e]  # Map key to corresponding value
        else:
            d[i] = None  # Map remaining keys to None if no corresponding value exists
    return d

# Driver code to test the createDict function
if __name__ == "__main__":
    keys = ['a', 'b', 'c', 'd']
    values = [1, 2, 3]
    
    result = createDict(keys, values)
    print(result)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': None}
