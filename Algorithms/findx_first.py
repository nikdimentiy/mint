def findx(seq, x):
    """Return the index of the first occurrence of x in seq.

    If x is not found, return -1.

    Parameters:
    seq (list): A list of elements
    x (any): The element to search for

    Returns:
    int: The index of x in seq or -1 if not found
    """

    ans = -1  # Initialize ans with -1
    for i in range(len(seq)):  # Loop through each index of seq
        if ans == -1 and seq[i] == x:  # If ans is -1 and current element is x
            ans = i  # Update ans with current index
    return ans  # Return ans


# Driver code to test findx function
l = ["foo", "bar", "baz"]  # Create a list l
print(findx(l, "bar"))  # Print the result of findx(l, "bar")
print(findx(l, "qux"))  # Print the result of findx(l, "qux")
