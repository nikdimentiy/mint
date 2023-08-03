  def list_find(lst, target):
    """
    Searches for the target element in the list and returns its index.

    Args:
        lst: The list to search.
        target: The element to search for.

    Returns:
        The index of the target element in the list, or -1 if the element is not found.
    """

    # Initialize the index to 0.
    index = 0

    # Iterate over the list until the target element is found or the end of the list is reached.
    while index < len(lst):
        # If the target element is found, break out of the loop.
        if lst[index] == target:
            break

        # Increment the index.
        index += 1

    # If the target element was not found, set the index to -1.
    else:
        index = -1

    # Return the index of the target element.
    return index

# Driver code to test the function
my_list = [10, 20, 30, 40, 50]
target_element = 33
result = list_find(my_list, target_element)

# Print the index of the target element.
print(f"The index of {target_element} in the list is: {result}")
