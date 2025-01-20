def unique_in_order(iterable):
    """
    Removes consecutive duplicates from an iterable while maintaining the original order.
    
    Args:
        iterable: Any iterable (string, list, tuple) containing elements that can be compared
    
    Returns:
        list: A new list with consecutive duplicates removed while preserving order
    
    Examples:
        >>> unique_in_order('AAAABBBCCDAABBB')
        ['A', 'B', 'C', 'D', 'A', 'B']
        >>> unique_in_order([1, 1, 1, 2, 2, 3, 1])
        [1, 2, 3, 1]
    """
    # Initialize empty result list
    result = []
    # Initialize previous element as None
    prev = None
    
    # Iterate through each element in the input iterable
    for char in iterable[0:]:
        # If current element is different from previous element
        if char != prev:
            # Add current element to result list
            result.append(char)
            # Update previous element
            prev = char
    return result

# Driver code
if __name__ == "__main__":
    # Test with string input
    print(unique_in_order('AAAABBBCCDAABBB'))  # ['A', 'B', 'C', 'D', 'A', 'B']
    
    # Test with list of numbers
    print(unique_in_order([1, 1, 1, 2, 2, 3, 1]))  # [1, 2, 3, 1]
    
    # Test with empty input
    print(unique_in_order(''))  # []
    
    # Test with list of mixed types
    print(unique_in_order(['A', 'A', 1, 1, 2, 'B', 'B']))  # ['A', 1, 2, 'B']
