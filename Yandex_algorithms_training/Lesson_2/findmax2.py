def findmax2(seq):
    """
    Find the two maximum values in a given sequence.

    Args:
        seq (list): A sequence of values.

    Returns:
        tuple: A tuple containing the two maximum values in the sequence.
    """
    # Initialize max1 and max2 with the first two elements of the sequence
    max1 = max(seq[0], seq[1])
    max2 = min(seq[0], seq[1])

    # Iterate through the sequence starting from index 2
    for i in range(2, len(seq)):
        # Check if the current element is greater than max1
        if seq[i] > max1:
            # Update max2 and max1 accordingly
            max2 = max1
            max1 = seq[i]
        # Check if the current element is greater than max2 but not greater than max1
        elif seq[i] > max2:
            # Update max2
            max2 = seq[i]

    return (max1, max2)

# Driver code to test the function
sequence = [3, 8, 2, 5, 10, 7]
result = findmax2(sequence)
print(f"The two maximum values in the sequence are: {result}")
