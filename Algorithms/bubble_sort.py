def bubble_sort(sequence):
    """
    Sorts a list in ascending order using the bubble sort algorithm.

    Args:
        sequence (list): The list to be sorted.

    Returns:
        list: The sorted list.
    """
    n = len(sequence)

    # Outer loop for each pass
    for i in range(n - 1):
        # Inner loop for comparisons and swaps
        for j in range(n - i - 1):
            # If the current element is greater than the next element, swap them
            if sequence[j] > sequence[j + 1]:
                sequence[j], sequence[j + 1] = sequence[j + 1], sequence[j]

    return sequence

# Driver code
if __name__ == "__main__":
    my_list = [1, 8, 6, 4, 1, 3, 0, 8, 9, 3, 7]
    result = bubble_sort(my_list)
    print("Sorted List:", result)

