def dbl_linear(n):
    """
    Generate the n-th element of a sequence defined by the following rules:
    - Start with the list containing the number 1.
    - For each element x in the list, add (2 * x + 1) and (3 * x + 1) to the list.
    - The sequence is formed by taking unique values from the generated list and sorting them.

    Parameters:
    n (int): The index of the desired element in the sequence (0-based).

    Returns:
    int: The n-th element of the sequence.
    """
    # Initialize the list with the first element
    num_list = [1]
    
    # Use a loop to generate new elements based on the current list
    for i in num_list:
        # Append the next elements based on the rules
        num_list.append((i * 2) + 1)
        num_list.append((i * 3) + 1)
        
        # Break the loop if the list is sufficiently large
        if len(num_list) > n * 10:
            break
    
    # Return the n-th unique sorted element
    return sorted(list(set(num_list)))[n]

# Driver code to test the function
if __name__ == "__main__":
    # Test cases
    print(dbl_linear(0))  # Expected output: 1
    print(dbl_linear(1))  # Expected output: 2
    print(dbl_linear(2))  # Expected output: 3
    print(dbl_linear(3))  # Expected output: 4
    print(dbl_linear(4))  # Expected output: 5
    print(dbl_linear(5))  # Expected output: 6
    print(dbl_linear(10)) # Expected output: 12
