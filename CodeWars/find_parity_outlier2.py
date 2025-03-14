def find_outlier(integers):
    """
    Find the single outlier integer in an array.
    
    This function takes an array of integers that is either entirely comprised
    of odd integers with one even outlier, or entirely comprised of even integers
    with one odd outlier. It returns the outlier.
    
    Args:
        integers (list): A list of integers with length >= 3, where all elements
                         are either odd or even except for exactly one outlier.
    
    Returns:
        int: The outlier integer that doesn't match the parity of the majority.
    
    Examples:
        >>> find_outlier([2, 4, 0, 100, 4, 11, 2602, 36])
        11
        >>> find_outlier([160, 3, 1719, 19, 11, 13, -21])
        160
    """
    listEven = []  # List to store even integers
    listOdd = []   # List to store odd integers
    
    # Iterate through all integers and separate them into even and odd lists
    for n in integers:
        if n % 2 == 0:  # Check if the number is even
            listEven.append(n)
        else:  # The number is odd
            listOdd.append(n)
    
    # Determine which list contains the outlier (the one with length 1)
    if len(listEven) == 1:
        return listEven[0]  # The outlier is the only even number
    else:
        return listOdd[0]   # The outlier is the only odd number


# Driver code to test the function
if __name__ == "__main__":
    # Test case 1: Array of even integers with one odd outlier
    test1 = [2, 4, 0, 100, 4, 11, 2602, 36]
    print(f"Test 1: {test1}")
    print(f"Outlier: {find_outlier(test1)}")  # Expected: 11
    
    # Test case 2: Array of odd integers with one even outlier
    test2 = [160, 3, 1719, 19, 11, 13, -21]
    print(f"\nTest 2: {test2}")
    print(f"Outlier: {find_outlier(test2)}")  # Expected: 160
    
    # Test case 3: Minimum length array with even outlier
    test3 = [1, 1, 2]
    print(f"\nTest 3: {test3}")
    print(f"Outlier: {find_outlier(test3)}")  # Expected: 2
    
    # Test case 4: Array with negative numbers
    test4 = [-3, -5, -7, -99, -97, -4]
    print(f"\nTest 4: {test4}")
    print(f"Outlier: {find_outlier(test4)}")  # Expected: -4
