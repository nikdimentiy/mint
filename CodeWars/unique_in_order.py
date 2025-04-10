def unique_in_order(iterable):
    """
    Returns a list of elements preserving the original order, but with consecutive duplicates removed.
    
    Args:
        iterable (iterable): A sequence (or any iterable) of elements (e.g., list, string)
                             which may include consecutive duplicate items.
    
    Returns:
        list: A new list with only the first occurrence of consecutive duplicates retained.
    
    Example:
        >>> unique_in_order('AAAABBBCCDAABBB')
        ['A', 'B', 'C', 'D', 'A', 'B']
    """
    # Convert the input iterable to a list for easy iteration.
    listofargs = list(iterable)
    uniqueList = []     # This will store the final unique elements.
    prevItem = None     # Initialize previous item.

    # Loop through each item in the list.
    for item in listofargs:
        # If the current item is the same as the previous, skip it.
        if item == prevItem:
            prevItem = item
            continue
        else:
            # Append unique item and update previous item.
            uniqueList.append(item)
            prevItem = item

    return uniqueList

# Driver code to test the function
if __name__ == "__main__":
    # Test cases
    test_string = 'AAAABBBCCDAABBB'
    expected_string_result = ['A', 'B', 'C', 'D', 'A', 'B']
    print("Test string input:", test_string)
    print("Output:", unique_in_order(test_string))
    print("Expected:", expected_string_result)
    
    test_list = [1, 2, 2, 3, 3, 3, 2, 2, 1]
    expected_list_result = [1, 2, 3, 2, 1]
    print("\nTest list input:", test_list)
    print("Output:", unique_in_order(test_list))
    print("Expected:", expected_list_result)
