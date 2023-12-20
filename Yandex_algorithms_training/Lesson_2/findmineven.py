def findmineven(seq):
    """
    Returns the smallest even number from the given sequence.

    Args:
        seq (list): A sequence of integers.

    Returns:
        int: The smallest even number in the sequence. Returns -1 if no even number is found.
    """
    ans = -1
    # Iterate through the sequence
    for i in range(len(seq)):
        # Check if the current element is even and smaller than the current answer
        if seq[i] % 2 == 0 and (ans == -1 or seq[i] < ans):
            ans = seq[i]

    return ans


# Driver code to test the function
sequence = [1, 3, 5, 9, 25, 6]
result = findmineven(sequence)
print(f"The smallest even number in the sequence is: {result}")
