def complete_series(seq):
    """
    Complete the series from 0 to the highest number in the input array of non-negative integers.

    If the input array contains duplicate values, the function will return a list containing only the value 0.
    If there are no duplicates, the function will return a list containing the complete series from 0 to the maximum value.

    Parameters:
    seq (list): A list of non-negative integers.

    Returns:
    list: A list containing either the complete series from 0 to the maximum value or [0] if duplicates are found.
    """
    # Check for duplicates by converting the list to a set and comparing lengths
    if len(set(seq)) < len(seq):
        return [0]  # Return [0] if there are duplicates
    else:
        # Return the complete series from 0 to the maximum value in the input list
        return list(range(0, max(seq) + 1))

# Driver code to test the function
if __name__ == "__main__":
    # Test cases
    print(complete_series([2, 1]))        # Output: [0, 1, 2]
    print(complete_series([1, 4, 4, 6]))  # Output: [0]
    print(complete_series([0, 3, 2]))     # Output: [0, 1, 2, 3]
    print(complete_series([5, 5, 5]))     # Output: [0]
    print(complete_series([3, 1, 2]))     # Output: [0, 1, 2, 3]
