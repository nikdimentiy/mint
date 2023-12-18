"""
This function finds the first index of a given element in a list.

Args:
    lst (list): The list to search in.
    X (any): The element to search for.

Returns:
    int: The index of the first occurrence of X in lst, or -1 if not found.
"""
def find_index(lst, X):
    """
    Initialize a variable 'index' to -1 to indicate not found yet.
    """
    index = -1

    """
    Loop through each element in the list using a for loop.
    """
    for i in range(len(lst)):
        """
        Check if the current element is equal to X and 'index' is still -1 (not found yet).
        """
        if lst[i] == X and index == -1:
            """
            If both conditions are met, update 'index' to the current element's index.
            Break the loop to stop searching after the first occurrence.
            """
            index = i
            break

    """
    Return the final value of 'index'.
    """
    return index

# Example usage
my_list = [1, 3, 5, 7, 9, 11]
X = 11

index = find_index(my_list, X)
print(index)  # Output: 5

my_list = [1, 3, 5, 7, 9, 11]
X = 12

index = find_index(my_list, X)
print(index)  # Output: -1
