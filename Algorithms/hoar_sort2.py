def hoar_sort(A):
    """
    Sorts an array using the Hoare partition scheme.

    Args:
        A: The array to be sorted.

    Returns:
        The sorted array.
    """

    # This is the doc string for the `hoar_sort` function. It explains what the function does and what its arguments and return values are.

    if len(A) <= 1:
        """
        If the array has one or fewer elements, it is already sorted, so return it.
        """
        return A

    barrier = A[0]
    """
    Select the first element of the array as the barrier.
    """
    L = [x for x in A if x < barrier]
    """
    Create a list `L` of all the elements in the array that are less than the barrier.
    """
    M = [x for x in A if x == barrier]
    """
    Create a list `M` of all the elements in the array that are equal to the barrier.
    """
    R = [x for x in A if x > barrier]
    """
    Create a list `R` of all the elements in the array that are greater than the barrier.
    """
    return hoar_sort(L) + M + hoar_sort(R)
    """
    Recursively sort the lists `L` and `R`, and then concatenate them together.
    """


# Example usage
arr = [4, 2, 1, 6, 8, 3, 5, 7]
"""
This is an example of how to use the `hoar_sort` function. It creates an array of integers and then sorts it using the `hoar_sort` function.
"""
sorted_arr = hoar_sort(arr)
print(sorted_arr)
"""
This line prints the sorted array.
"""
