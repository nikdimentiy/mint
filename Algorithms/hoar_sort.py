def hoar_sort(A):
    """
    Sorts an array using Hoare's partition scheme.

    Args:
        A: The array to be sorted.

    Returns:
        The sorted array.
    """

    """This doc string explains what the `hoar_sort` function does and what its arguments and return values are."""

    # Check if the array is empty or has only one element. If it is, simply return the array.

    if len(A) <= 1:
        return A

    # The variable `barrier` will be used to partition the array.

    barrier = A[0]

    # Create three empty lists, `L`, `M`, and `R`, to store the elements of the array that are less than, equal to, and greater than the barrier, respectively.

    L = []  # elements less than barrier
    M = []  # elements equal to barrier
    R = []  # elements greater than barrier

    # Iterate over the elements of the array and add them to the appropriate list based on their value relative to the barrier.

    for x in A:
        if x < barrier:
            L.append(x)
        elif x == barrier:
            M.append(x)
        else:
            R.append(x)

    # Recursively sort the lists `L` and `R` and then concatenate them with the element equal to the barrier to form the sorted array.

    return hoar_sort(L) + M + hoar_sort(R)


# Example usage

arr = [4, 2, 1, 6, 8, 3, 5, 7]
sorted_arr = hoar_sort(arr)
print(sorted_arr)

# This line prints the sorted array.
