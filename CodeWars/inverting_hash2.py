def invert_hash(dictionary):
    """
    Invert a given dictionary by swapping its keys and values.

    Args:
        dictionary (dict): A dictionary with unique values.

    Returns:
        dict: A new dictionary with keys and values swapped.
    
    Example:
        Given the input:
        { 'a' : 1, 'b' : 2, 'c' : 3 }
        
        The output will be:
        { 1 : 'a', 2 : 'b', 3 : 'c' }
    """
    # Initialize an empty dictionary to store the inverted key-value pairs
    inverted_dict = {}
    
    # Iterate through each key in the original dictionary
    for key in dictionary:
        # Swap the key and value and store them in the inverted dictionary
        inverted_dict[dictionary[key]] = key
    
    # Return the inverted dictionary
    return inverted_dict

# Driver code to test the invert_hash function
if __name__ == "__main__":
    # Test case 1
    input_dict1 = { 'a': 1, 'b': 2, 'c': 3 }
    output_dict1 = invert_hash(input_dict1)
    print("Input:", input_dict1)
    print("Inverted Output:", output_dict1)

    # Test case 2
    input_dict2 = { 'foo': 'bar', 'hello': 'world' }
    output_dict2 = invert_hash(input_dict2)
    print("Input:", input_dict2)
    print("Inverted Output:", output_dict2)
