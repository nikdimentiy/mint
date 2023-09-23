def count_positives_sum_negatives(arr):
    """
    Count the number of positive elements and calculate the sum of negative elements in a list.

    Args:
    arr (list of int): The input list of integers.

    Returns:
    list of int: A list containing two integers:
        - The count of positive elements in the input list.
        - The sum of negative elements in the input list.
    
    Example:
    >>> count_positives_sum_negatives([1, 2, -3, 4, -5])
    [2, -8]
    >>> count_positives_sum_negatives([])
    []
    """

    # Initialize counters for positive and negative numbers.
    count_positive = 0
    sum_negative = 0

    # Iterate through the elements in the input list.
    for num in arr:
        if num > 0:
            # Increment the count of positive elements.
            count_positive += 1
        elif num < 0:
            # Add the negative number to the sum of negative elements.
            sum_negative += num

    # Return the count of positive elements and the sum of negative elements as a list.
    return [count_positive, sum_negative]


# Driver code
if __name__ == "__main__":
    input_list = [int(x) for x in input("Enter a list of integers separated by spaces: ").split()]
    result = count_positives_sum_negatives(input_list)
    print("Count of positive elements:", result[0])
    print("Sum of negative elements:", result[1])

