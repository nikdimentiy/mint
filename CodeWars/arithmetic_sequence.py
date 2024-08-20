def arithmetic_sequence_elements(a, d, n):
    """
    Generate the first n elements of an arithmetic progression.

    Parameters:
    a (int): The first element of the sequence.
    d (int): The common difference between consecutive elements.
    n (int): The number of elements to generate.

    Returns:
    str: A string representation of the first n elements of the arithmetic sequence,
         separated by a comma and a space.
    """
    # Generate the sequence using list comprehension
    sequence = [a + (i * d) for i in range(n)]
    
    # Join the sequence elements into a string separated by comma and space
    return ", ".join(str(i) for i in sequence)

# Driver code to test the function
if __name__ == "__main__":
    # Test cases
    print(arithmetic_sequence_elements(1, 2, 5))  # Expected output: "1, 3, 5, 7, 9"
    print(arithmetic_sequence_elements(0, 0, 5))  # Expected output: "0, 0, 0, 0, 0"
    print(arithmetic_sequence_elements(3, -1, 5))  # Expected output: "3, 2, 1, 0, -1"
    print(arithmetic_sequence_elements(5, 5, 5))  # Expected output: "5, 10, 15, 20, 25"
    print(arithmetic_sequence_elements(10, -2, 4))  # Expected output: "10, 8, 6, 4"
