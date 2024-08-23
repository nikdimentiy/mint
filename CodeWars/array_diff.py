def array_diff(a, b):
    """
    Returns a new list containing elements from list 'a' that are not present in list 'b'.

    Parameters:
    a (list): The list from which elements will be filtered.
    b (list): The list containing elements to be excluded from 'a'.

    Returns:
    list: A list containing elements from 'a' that are not in 'b'.
    """
    # Use a list comprehension to filter out elements in 'a' that are also in 'b'
    return [x for x in a if x not in b]

# Driver code to test the array_diff function
if __name__ == "__main__":
    # Test cases
    a = [1, 2, 3, 4, 5]
    b = [2, 4]
    
    # Expected output: [1, 3, 5]
    result = array_diff(a, b)
    print("Result of array_diff(a, b):", result)

    # Additional test cases
    a2 = ['apple', 'banana', 'cherry']
    b2 = ['banana']
    
    # Expected output: ['apple', 'cherry']
    result2 = array_diff(a2, b2)
    print("Result of array_diff(a2, b2):", result2)

    a3 = [1, 2, 3]
    b3 = []
    
    # Expected output: [1, 2, 3] (since b is empty)
    result3 = array_diff(a3, b3)
    print("Result of array_diff(a3, b3):", result3)

    a4 = []
    b4 = [1, 2, 3]
    
    # Expected output: [] (since a is empty)
    result4 = array_diff(a4, b4)
    print("Result of array_diff(a4, b4):", result4)
