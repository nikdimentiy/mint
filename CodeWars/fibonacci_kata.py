def calc(n):
    """
    Helper function to calculate Fibonacci numbers using the fast doubling method.
    
    This function returns a tuple (F(n), F(n+1)) where F(n) is the nth Fibonacci number.
    
    Parameters:
    n (int): The index of the Fibonacci number to calculate.
    
    Returns:
    tuple: A tuple containing F(n) and F(n+1).
    """
    if n == 0:
        return (0, 1)  # Base case: F(0) = 0, F(1) = 1
    elif n == 1:
        return (1, 1)  # Base case: F(1) = 1, F(2) = 1
    else:
        a, b = calc(n // 2)  # Recursively calculate F(n // 2) and F(n // 2 + 1)
        p = a * (2 * b - a)  # F(2k) = F(k) * (2*F(k+1) - F(k))
        q = b * b + a * a    # F(2k + 1) = F(k+1)^2 + F(k)^2
        return (p, q) if n % 2 == 0 else (q, p + q)  # Return the appropriate Fibonacci numbers


def fib(n):
    """
    Calculates the nth Fibonacci number.
    
    This function handles both positive and negative indices using the property
    that F(-n) = (-1)^(n+1) * F(n) for negative indices.
    
    Parameters:
    n (int): The index of the Fibonacci number to calculate.
    
    Returns:
    int: The nth Fibonacci number.
    """
    if n >= 0:
        return calc(n)[0]  # For non-negative n, return F(n)
    else:
        return -calc(-n)[0] if n % 2 == 0 else calc(-n)[0]  # For negative n, apply the sign rule


# Driver code to test the Fibonacci function
if __name__ == "__main__":
    # Test cases for the Fibonacci function
    test_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5]
    
    for n in test_values:
        print(f"Fibonacci({n}) = {fib(n)}")
