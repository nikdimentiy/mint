def complete_series(seq):
    """
    Complete the series from 0 to the highest number in the input array.
    
    If the input array contains duplicate values, return a list containing only the value 0.
    Otherwise, return a list of integers from 0 to the maximum value in the array.
    
    Parameters:
    seq (list of int): A list of non-negative integers.
    
    Returns:
    list: A list containing the complete series or [0] if duplicates are found.
    """
    # Check if there are duplicates in the input sequence
    if len(set(seq)) != len(seq):
        return [0]  # Return [0] if duplicates are found
    
    # If no duplicates, return the complete series from 0 to the maximum value
    return list(range(0, max(seq) + 1))

# Driver code to test the function
if __name__ == "__main__":
    # Test cases
    print(complete_series([2, 1]))        # Output: [0, 1, 2]
    print(complete_series([1, 4, 4, 6]))  # Output: [0]
    print(complete_series([0, 3, 2]))     # Output: [0, 1, 2, 3]
    print(complete_series([5, 5, 5]))     # Output: [0]
    print(complete_series([3, 1, 2]))     # Output: [0, 1, 2, 3]
