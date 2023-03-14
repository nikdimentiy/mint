def solution(n):
    """Check if n is a power of some integer.

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
    if n == 1:  # if n is equal to 1
        return True  # return True and end the function
    # loop through the numbers from 2 to the square root of n rounded up
    for i in range(2, int(n**(0.5))+1):
        x = i  # assign i to a variable x
        while x <= n:  # while x is less than or equal to n
            x *= i  # multiply x by i
            if x == n:  # if x is equal to n
                return True  # return True and end the function
    return False  # if none of the above conditions are met, return False and end the function
