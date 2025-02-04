def solution(n):
    """
    Returns the largest number that contains exactly n digits.

    The largest n-digit number is formed by having all digits as 9.
    For example:
    - If n = 1, the largest 1-digit number is 9.
    - If n = 2, the largest 2-digit number is 99.
    - If n = 3, the largest 3-digit number is 999.

    Parameters:
    n (int): The number of digits.

    Returns:
    int: The largest number with exactly n digits.
    """
    # Calculate the largest n-digit number
    return 10**n - 1

# Driver code to test the solution function
if __name__ == "__main__":
    # Test cases
    for i in range(1, 6):
        print(f"The largest number with {i} digits is: {solution(i)}")
