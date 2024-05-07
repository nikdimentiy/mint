def child_addition(param1, param2):
    """
    Simulates the addition of two integers as if a child performed the addition 
    without considering carry-over between columns.

    Given two integers `param1` and `param2`, this function adds them digit-by-digit 
    without considering the carry. The result is a new integer with each digit being 
    the modulo 10 sum of the corresponding digits from the input integers.

    :param param1: First integer to add
    :param param2: Second integer to add
    :return: Integer resulting from digit-by-digit addition without carry
    """
    result = 0  # Initialize the result
    factor = 1  # Used to keep track of the place value (units, tens, etc.)
    
    # Continue until both input numbers have been processed
    while param1 > 0 or param2 > 0:
        # Get the last digit of each input number
        digit1 = param1 % 10
        digit2 = param2 % 10
        
        # Compute the modulo 10 sum for the current digit place
        digit_sum = (digit1 + digit2) % 10
        
        # Add the digit sum to the result at the correct place value
        result += digit_sum * factor
        
        # Update the factor to move to the next place value (tens, hundreds, etc.)
        factor *= 10
        
        # Remove the last digit from each input number
        param1 //= 10
        param2 //= 10
    
    return result


# Driver code to test the child_addition function
if __name__ == "__main__":
    test_cases = [
        (123, 456),  # Expected: 579 (because there's no carry)
        (88, 44),    # Expected: 22 (8 + 4 = 12, but we ignore the carry, so it becomes 2)
        (345, 678),  # Expected: 903
        (99, 99),    # Expected: 88 (because 9+9=18, without carry becomes 8)
    ]
    
    # Test the function with the given test cases
    for param1, param2 in test_cases:
        result = child_addition(param1, param2)
        print(f"child_addition({param1}, {param2}) = {result}")
