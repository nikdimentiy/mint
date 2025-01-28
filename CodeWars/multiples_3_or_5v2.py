def solution(number):
    """
    Calculates the sum of all multiples of 3 or 5 below the given number.

    Args:
        number (int): The upper limit (exclusive) for calculating the sum of multiples.

    Returns:
        int: The sum of all multiples of 3 or 5 below the number, or 0 if the number is negative.
    """
    # If the number is negative, return 0
    if number < 0:
        return 0

    # Initialize the sum to 0
    total_sum = 0

    # Loop through all the natural numbers below the number
    for i in range(1, number):
        # If the number is a multiple of 3 or 5, add it to the sum
        if i % 3 == 0 or i % 5 == 0:
            total_sum += i

    # Return the sum
    return total_sum

# Driver code
if __name__ == "__main__":
    # Test cases
    print(solution(10))   # Output: 23 (3 + 5 + 6 + 9)
    print(solution(20))   # Output: 78 (3 + 5 + 6 + 9 + 10 + 12 + 15 + 18)
    print(solution(-5))   # Output: 0 (negative number)
    print(solution(0))    # Output: 0 (no positive multiples)
