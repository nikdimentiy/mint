def calc(x):
    """
    Calculate the difference between the sum of ASCII values of characters in a string
    and the sum of ASCII values after replacing all occurrences of '7' with '1'.

    Parameters:
    x (str): The input string for which the calculation is performed.

    Returns:
    int: The difference between the two sums.
    """
    # Convert each character in the string to its ASCII value and join them as a string
    total1 = "".join([str(ord(i)) for i in x])
    
    # Replace all occurrences of '7' with '1' in the ASCII string
    total2 = total1.replace("7", "1")
    
    # Calculate the sum of the ASCII values in the original string
    sum1 = sum([int(i) for i in total1])
    
    # Calculate the sum of the ASCII values in the modified string
    sum2 = sum([int(i) for i in total2])
    
    # Return the difference between the two sums
    return sum1 - sum2

# Driver code to test the function
if __name__ == "__main__":
    test_string = "Hello, World!"
    result = calc(test_string)
    print(f"The difference for the input '{test_string}' is: {result}")
