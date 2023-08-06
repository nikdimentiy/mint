# 🎯 Preparation to algorithmic interview (coding) interview 🍀

def countsort(seq):
    """
    Sorts a list of integers using Counting Sort algorithm.

    Parameters:
        seq (list[int]): The input list of integers to be sorted.

    Returns:
        None: The function modifies the input list in-place and does not return anything.
    """
    minval = min(seq)  # Find the minimum value in the input list
    maxval = max(seq)  # Find the maximum value in the input list
    k = maxval - minval + 1  # Calculate the range of values in the input list
    count = [0] * k  # Initialize a count array to keep track of occurrences of each value

    # Count the occurrences of each value in the input list
    for num in seq:
        count[num - minval] += 1

    nowpos = 0  # Variable to keep track of the current position in the original list
    # Reconstruct the sorted sequence using the counts
    for val in range(k):
        for i in range(count[val]):
            seq[nowpos] = val + minval
            nowpos += 1

# Driver code
if __name__ == "__main__":
    input_seq = [4, 2, 2, 8, 3, 3, 1]
    print("Original Sequence:", input_seq)
    countsort(input_seq)
    print("Sorted Sequence:", input_seq)
