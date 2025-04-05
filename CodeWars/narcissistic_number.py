def is_narcissistic_number(number):
    """
    Determines whether a given number is a Narcissistic Number (or Armstrong Number).
    
    A Narcissistic Number is a positive number which is equal to the sum of its own digits,
    each raised to the power of the number of digits in the number.
    
    Parameters:
    ----------
    number : int
        The number to check for being a Narcissistic Number.
        
    Returns:
    -------
    bool
        True if the number is a Narcissistic Number, False otherwise.
    
    Example:
    --------
    >>> is_narcissistic_number(153)
    True
    Explanation: 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
    
    >>> is_narcissistic_number(9474)
    True
    Explanation: 9^4 + 4^4 + 7^4 + 4^4 = 6561 + 256 + 2401 + 256 = 9474
    """
    # Convert the number to a string to easily access individual digits
    num_str = str(number)
    
    # Determine the number of digits in the number
    n = len(num_str)
    
    # Compute the sum of each digit raised to the power of `n`
    total = sum(int(digit)**n for digit in num_str)
    
    # Check if the computed sum equals the original number
    return total == number

# Driver code to test the function
if __name__ == "__main__":
    # Test cases
    test_numbers = [153, 9474, 9475, 370, 371, 407]
    
    print("Testing Narcissistic Number Function:")
    for num in test_numbers:
        result = is_narcissistic_number(num)
        print(f"{num} is a Narcissistic Number: {result}")
