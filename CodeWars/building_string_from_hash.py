def solution(pairs):
    """
    Generates a human-readable string from the key/value pairs of a dictionary.

    The format of the output string is "KEY = VALUE", where each key/value pair
    is separated by a comma. The key/value pairs are sorted by key in ascending order.

    Args:
        pairs (dict): A dictionary containing key/value pairs.

    Returns:
        str: A formatted string representing the key/value pairs.
    """
    # Create a list of formatted key/value pairs
    formatted_pairs = ["{} = {}".format(k, v) for k, v in pairs.items()]
    
    # Sort the formatted pairs by key
    sorted_pairs = sorted(formatted_pairs)
    
    # Join the sorted pairs with a comma and return the result
    return ",".join(sorted_pairs)

# Driver code to test the solution
if __name__ == "__main__":
    # Example dictionary to test the function
    test_pairs = {
        'name': 'Alice',
        'age': 30,
        'city': 'Wonderland',
        'occupation': 'Adventurer'
    }
    
    # Call the solution function and print the result
    result = solution(test_pairs)
    print(result)  # Expected output: "age = 30,city = Wonderland,name = Alice,occupation = Adventurer"
