def primeFactors(n):
    """
    Compute the prime factorization of a positive integer.
    
    This function finds all prime factors of the input number and returns
    them in a string format like: (2)(3**2)(5) for the number 90.
    
    Args:
        n (int): A positive integer greater than 1
        
    Returns:
        str: A string representation of the prime factorization
             in the format (p1)(p2**k2)...(pn**kn) where p1, p2, ..., pn are
             prime factors and k2, ..., kn are their respective powers when > 1
             
    Raises:
        ValueError: If n is not a positive integer greater than 1
    """
    # Input validation
    if not isinstance(n, int) or n <= 1:
        raise ValueError("Input must be a positive integer greater than 1")
    
    i = 2  # Start with the smallest prime number
    r = ''  # Initialize the result string
    
    while n != 1:
        k = 0  # Counter for the power of the current factor
        
        # Count how many times i divides n
        while n % i == 0:
            n = n / i
            k += 1
        
        # Add the factor to the result string according to its power
        if k == 1:
            r = r + '(' + str(i) + ')'
        elif k == 0:
            pass  # If i is not a factor, do nothing
        else:
            r = r + '(' + str(i) + '**' + str(k) + ')'
        
        i += 1  # Move to the next potential factor
    
    return r

# Driver code
if __name__ == "__main__":
    # Test with some example numbers
    test_cases = [2, 3, 4, 12, 24, 36, 48, 60, 90, 100, 999]
    
    for num in test_cases:
        print(f"Prime factorization of {num}: {primeFactors(num)}")
