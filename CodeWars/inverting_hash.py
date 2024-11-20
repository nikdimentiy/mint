def invert_hash(dictionary):
    """
    Invert a given dictionary by swapping its keys and values.

    Args:
        dictionary (dict): A dictionary with unique values.

    Returns:
        dict: A new dictionary with keys and values swapped.
    
    Example:
        Given the input:
        {'a': 1, 'b': 2, 'c': 3}
        
        The output will be:
        {1: 'a', 2: 'b', 3: 'c'}
    """
    # Create a new dictionary by swapping keys and values
    return {v: k for k, v in dictionary.items()}

# Driver code to test the invert_hash function
if __name__ == "__main__":
    # Test case 1
    input_dict1 = {'a': 1, 'b': 2, 'c': 3}
    inverted_dict1 = invert_hash(input_dict1)
    print("Inverted Dictionary 1:", inverted_dict1)  # Expected: {1: 'a', 2: 'b', 3: 'c'}

    # Test case 2
    input_dict2 = {'foo': 'bar', 'hello': 'world'}
    inverted_dict2 = invert_hash(input_dict2)
    print("Inverted Dictionary 2:", inverted_dict2)  # Expected: {'bar': 'foo', 'world': 'hello'}
