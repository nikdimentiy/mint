def is_prime(n):
    """
    Check if a number is prime using 6k ± 1 optimization.
    
    This function implements an efficient primality test by:
    1. Handling basic cases (n ≤ 1, n ≤ 3, even numbers, multiples of 3)
    2. Using the fact that all primes > 3 can be written in form 6k ± 1
    3. Only checking divisors up to square root of n
    
    Args:
        n (int): The number to test for primality
        
    Returns:
        bool: True if the number is prime, False otherwise
        
    Examples:
        >>> is_prime(17)
        True
        >>> is_prime(24)
        False
    """
    # Handle special cases
    if n <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    elif n <= 3:
        return True   # 2 and 3 are prime numbers
    elif n % 2 == 0 or n % 3 == 0:
        return False  # Even numbers > 2 and multiples of 3 are not prime
    
    # Loop through possible divisors (6k ± 1)
    # We only need to check up to sqrt(n)
    # All primes > 3 can be written in form 6k ± 1
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False  # Found a divisor, so n is not prime
        i += 6  # Move to next potential divisor pair (6k ± 1)
    
    # If no divisors found, n is prime
    return True

# Driver code to test the function
def test_is_prime():
    # Test basic cases
    assert not is_prime(1), "1 should not be prime"
    assert is_prime(2), "2 should be prime"
    assert is_prime(3), "3 should be prime"
    
    # Test non-prime numbers
    assert not is_prime(4), "4 should not be prime"
    assert not is_prime(6), "6 should not be prime"
    assert not is_prime(15), "15 should not be prime"
    
    # Test prime numbers
    assert is_prime(5), "5 should be prime"
    assert is_prime(7), "7 should be prime"
    assert is_prime(17), "17 should be prime"
    assert is_prime(23), "23 should be prime"
    
    # Test larger numbers
    assert not is_prime(100), "100 should not be prime"
    assert is_prime(997), "997 should be prime"
    
    print("All test cases passed!")

# Run the tests
if __name__ == "__main__":
    test_is_prime()
    
    # Additional examples
    test_numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 29, 31]
    for num in test_numbers:
        print(f"Is {num} prime? {is_prime(num)}")
