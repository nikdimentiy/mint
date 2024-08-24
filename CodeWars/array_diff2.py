def array_diff(a, b):
    """
    Remove all elements from list 'a' that are present in list 'b'.

    Parameters:
    a (list): The list from which elements will be removed.
    b (list): The list containing elements to be removed from 'a'.

    Returns:
    list: A new list containing elements from 'a' that are not in 'b'.
    """
    # Iterate through each element in list 'b'
    for i in range(len(b)):
        # While the current element of 'b' is in 'a', remove it from 'a'
        while b[i] in a:
            a.remove(b[i])
    return a

# Driver code to test the array_diff function
if __name__ == "__main__":
    # Example lists
    a = [1, 2, 2, 3, 4]
    b = [2, 3]

    # Call the array_diff function
    result = array_diff(a, b)

    # Print the result
    print("Resulting list after removing elements:", result)
