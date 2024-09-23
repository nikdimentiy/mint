import random

def even_odd(n):
    """
    Decomposes n-1 into the form 2^s * d where d is odd.
    
    Parameters:
    n (int): The number to decompose.
    
    Returns:
    tuple: A tuple (s, d) where s is the exponent of 2 and d is the odd component.
    """
    s, d = 0, n
    while d % 2 == 0:
        s += 1
        d >>= 1  # Equivalent to d //= 2
    return s, d

def Miller_Rabin(a, p):
    """
    Performs the Miller-Rabin primality test for a given base a and number p.
    
    Parameters:
    a (int): The base to test.
    p (int): The number to test for primality.
    
    Returns:
    bool: True if p is probably prime, False if p is composite.
    """
    s, d = even_odd(p - 1)  # Decompose p-1
    a = pow(a, d, p)  # Compute a^d mod p
    if a == 1:
        return True  # a^d ≡ 1 (mod p) indicates p may be prime
    for i in range(s):
        if a == p - 1:
            return True  # a^(2^i * d) ≡ -1 (mod p) indicates p may be prime
        a = pow(a, 2, p)  # Square a for the next iteration
    return False  # If none of the conditions are met, p is composite

def is_prime(p):
    """
    Determines if a number p is prime using the Miller-Rabin test.
    
    Parameters:
    p (int): The number to test for primality.
    
    Returns:
    bool: True if p is probably prime, False if p is composite.
    """
    if p == 2:
        return True  # 2 is prime
    if p <= 1 or p % 2 == 0:
        return False  # Exclude even numbers and numbers <= 1
    # Perform the Miller-Rabin test with 40 iterations for accuracy
    return all(Miller_Rabin(random.randint(2, p - 1), p) for _ in range(40))

# Driver code to test the is_prime function
if __name__ == "__main__":
    test_numbers = [2, 3, 4, 5, 10, 11, 15, 17, 19, 23, 24, 29, 31, 37, 41, 43, 97, 100, 101, 103, 104729]
    
    for number in test_numbers:
        result = is_prime(number)
        print(f"{number} is {'prime' if result else 'not prime'}")
