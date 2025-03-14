def arithmetic_sequence_elements(a, d, n):
    """
    Generate a string representation of the first n elements of an arithmetic sequence.
    
    An arithmetic sequence is a sequence of numbers such that the difference between
    the consecutive terms is constant (the common difference).
    
    Args:
        a (int): First element of the sequence
        d (int): Common difference between consecutive elements
        n (int): Number of elements to generate
        
    Returns:
        str: String of sequence elements separated by comma and space
        
    Examples:
        >>> arithmetic_sequence_elements(1, 2, 5)
        "1, 3, 5, 7, 9"
        >>> arithmetic_sequence_elements(0, 0, 5)
        "0, 0, 0, 0, 0"
    """
    sequence = []  # create an empty list to store sequence elements
    
    for i in range(n):
        current_element = a + (i * d)  # calculate the current element using the formula: a + i*d
        sequence.append(str(current_element))  # convert to string and add to our sequence list
    
    # join all elements with comma and space separator
    return ", ".join(sequence)


# Driver code to test the function
if __name__ == "__main__":
    # Test case 1: Positive first element, positive difference
    print("Test case 1:")
    print(f"a=1, d=2, n=5 → {arithmetic_sequence_elements(1, 2, 5)}")
    # Expected output: "1, 3, 5, 7, 9"
    
    # Test case 2: Zero first element, zero difference (constant sequence)
    print("\nTest case 2:")
    print(f"a=0, d=0, n=5 → {arithmetic_sequence_elements(0, 0, 5)}")
    # Expected output: "0, 0, 0, 0, 0"
    
    # Test case 3: Positive first element, negative difference (decreasing sequence)
    print("\nTest case 3:")
    print(f"a=3, d=-1, n=5 → {arithmetic_sequence_elements(3, -1, 5)}")
    # Expected output: "3, 2, 1, 0, -1"
    
    # Test case 4: Negative first element, positive difference
    print("\nTest case 4:")
    print(f"a=-5, d=3, n=6 → {arithmetic_sequence_elements(-5, 3, 6)}")
    # Expected output: "-5, -2, 1, 4, 7, 10"
