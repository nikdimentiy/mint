def findx_last(seq, x):
    """Return the index of the last occurrence of x in seq.

    If x is not found, return -1.

    Parameters:
    seq (list): A list of elements
    x (any): The element to search for

    Returns:
    int: The index of x in seq or -1 if not found
    """
    
    try: # Try to find the index of x in reversed seq
        ans = len(seq) - 1 - seq[::-1].index(x) # Calculate the index from last
    except ValueError: # If x is not found
        ans = -1 # Set ans to -1
    return ans # Return ans

# Driver code to test findx_last function
l = ["foo", "bar", "baz", "bar"] # Create a list l
print(findx_last(l, "bar")) # Print the result of findx_last(l, "bar")
print(findx_last(l, "qux")) # Print the result of findx_last(l, "qux")