def stray(arr):
    """
    Find the unique number in an array where all other numbers appear exactly twice.
    
    This function searches through an array and returns the element that appears
    exactly once, assuming all other elements appear exactly twice.
    
    Args:
        arr (list): A list of numbers where all numbers except one appear exactly 
                   twice. The list must contain at least 3 elements.
    
    Returns:
        The number that appears only once in the array.
    
    Example:
        >>> stray([1, 1, 2])
        2
        >>> stray([17, 17, 3, 17, 17, 17, 17])
        3
    """
    # Iterate through each element in the array
    for x in arr:
        # Check if the current element appears exactly once
        if arr.count(x) == 1:
            # Return the element that appears only once
            return x


# Driver code to test the function
if __name__ == "__main__":
    # Test case 1: Basic case with 3 elements
    test1 = [1, 1, 2]
    print(f"Test 1: {test1} -> {stray(test1)}")  # Expected output: 2
    
    # Test case 2: Multiple duplicates with one unique element
    test2 = [17, 17, 3, 17, 17, 17, 17]
    print(f"Test 2: {test2} -> {stray(test2)}")  # Expected output: 3
    
    # Test case 3: Unique element at the beginning
    test3 = [8, 1, 1, 1, 1, 1, 1]
    print(f"Test 3: {test3} -> {stray(test3)}")  # Expected output: 8
    
    # Test case 4: Unique element at the end
    test4 = [4, 4, 4, 4, 4, 9]
    print(f"Test 4: {test4} -> {stray(test4)}")  # Expected output: 9
    
    # Test case 5: Negative numbers
    test5 = [-6, -6, -6, -6, -6, -5, -6]
    print(f"Test 5: {test5} -> {stray(test5)}")  # Expected output: -5
