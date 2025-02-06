def solution(n):
    """
    Check if n is a power of some integer greater than 1.

    A number n is considered a power of an integer if there exists an integer 
    x > 1 such that x^k = n for some integer k >= 1.

    Args:
        n (int): A positive integer.

    Returns:
        bool: True if n is a power of some integer greater than 1, False otherwise.

    Examples:
        >>> solution(1)
        True
        >>> solution(4)
        True
        >>> solution(6)
        False
    """
    if n == 1:  # If n is equal to 1, it is considered a power (1^k for any k)
        return True  # Return True and end the function

    # Loop through potential base integers from 2 to the square root of n
    for i in range(2, int(n**(0.5)) + 1):
        x = i  # Start with the base integer i
        while x <= n:  # While x is less than or equal to n
            x *= i  # Multiply x by i (i.e., calculate i^k)
            if x == n:  # If x equals n, then n is a power of i
                return True  # Return True and end the function

    return False  # If no base integer satisfies the condition, return False


# Driver code to test the solution function
if __name__ == "__main__":
    # Test cases
    test_cases = [1, 4, 6, 8, 9, 10, 16, 27, 32, 64, 100]
    
    for n in test_cases:
        result = solution(n)
        print(f"solution({n}) = {result}")
