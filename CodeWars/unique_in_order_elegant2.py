def unique_in_order(iterable):
    """
    This function takes an iterable (e.g., list, string, tuple) and returns a list of its elements
    with consecutive duplicates removed. The order of unique elements is preserved.

    Parameters:
    iterable (iterable): An iterable object (e.g., list, string, tuple).

    Returns:
    list: A list containing the elements of the input iterable with consecutive duplicates removed.

    Example:
    >>> unique_in_order('AAAABBBCCDAABBB')
    ['A', 'B', 'C', 'D', 'A', 'B']
    >>> unique_in_order([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
    [1, 2, 3, 4]
    """
    # Initialize an empty list to store the result
    res = []

    # Iterate through each item in the input iterable
    for item in iterable:
        # If the result list is empty or the current item is not equal to the last item in the result
        if len(res) == 0 or item != res[-1]:
            # Append the current item to the result list
            res.append(item)

    # Return the final list with consecutive duplicates removed
    return res


# Driver code to test the function
if __name__ == "__main__":
    # Example 1: String input
    input1 = "AAAABBBCCDAABBB"
    print(f"Input: {input1}")
    print(f"Output: {unique_in_order(input1)}\n")

    # Example 2: List input with integers
    input2 = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    print(f"Input: {input2}")
    print(f"Output: {unique_in_order(input2)}\n")

    # Example 3: Tuple input
    input3 = ('a', 'b', 'b', 'c', 'c', 'd', 'd', 'd')
    print(f"Input: {input3}")
    print(f"Output: {unique_in_order(input3)}\n")

    # Example 4: Empty input
    input4 = ""
    print(f"Input: {input4}")
    print(f"Output: {unique_in_order(input4)}\n")

    # Example 5: Single-element input
    input5 = [42]
    print(f"Input: {input5}")
    print(f"Output: {unique_in_order(input5)}")
