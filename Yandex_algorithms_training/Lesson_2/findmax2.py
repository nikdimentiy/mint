def findmax2(seq):
    """
    Find the two maximum values in a list of integers.
    Returns a tuple (max1, max2), where max1 is the maximum value and max2 is the second maximum value.
    If there is only one unique maximum value, max2 is set to None.
    """
    if len(seq) < 2:
        return None, None
    
    max1: int = seq[0]
    max2: int | None = None
    
    for x in seq[1:]:
        if x > max1:
            max2 = max1
            max1 = x
        elif max2 is None or (x > max2 and x != max1):
            max2 = x
    
    return max1, max2

# Driver code
if __name__ == "__main__":
    # Test case 1: List with unique elements
    seq1 = [10, 5, 8, 20, 15]
    print(f"Input: {seq1}")
    max1, max2 = findmax2(seq1)
    print(f"Output: max1 = {max1}, max2 = {max2}")  # Output: max1 = 20, max2 = 15

    print()

    # Test case 2: List with duplicate elements
    seq2 = [10, 20, 30, 20, 15]
    print(f"Input: {seq2}")
    max1, max2 = findmax2(seq2)
    print(f"Output: max1 = {max1}, max2 = {max2}")  # Output: max1 = 30, max2 = 20

    print()

    # Test case 3: List with only one unique maximum value
    seq3 = [10, 20, 20, 20, 20]
    print(f"Input: {seq3}")
    max1, max2 = findmax2(seq3)
    print(f"Output: max1 = {max1}, max2 = {max2}")  # Output: max1 = 20, max2 = None
