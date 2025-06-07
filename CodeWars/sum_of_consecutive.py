def solution(n):
    """
    Counts the number of ways to express a positive integer n as a sum of consecutive positive integers.

    A sum of consecutive positive integers can be represented as:
    k + (k + 1) + (k + 2) + ... + (k + m) = n
    where k is the starting integer and m is the number of terms.

    Parameters:
    n (int): The positive integer to be expressed as a sum.

    Returns:
    int: The number of ways to express n as a sum of consecutive positive integers.
    """
    
    start, end = 1, 1  # Initialize start and end variables to 1
    current_sum = 1  # Initialize current_sum variable to 1
    count = 0  # Initialize count variable to 0

    while start < n:  # Loop until start reaches n
        if current_sum == n:  # If the current_sum is equal to n
            count += 1  # Increment the count by 1
            current_sum -= start  # Subtract the start from the current_sum
            start += 1  # Increment the start by 1
        elif current_sum < n:  # If the current_sum is less than n
            end += 1  # Increment the end by 1
            current_sum += end  # Add the end to the current_sum
        else:  # If the current_sum is greater than n
            current_sum -= start  # Subtract the start from the current_sum
            start += 1  # Increment the start by 1

    return count  # Return the final count


# Driver code to test the solution function
if __name__ == "__main__":
    test_values = [1, 3, 5, 6, 10, 15, 20]
    for value in test_values:
        result = solution(value)
        print(f"The number of ways to express {value} as a sum of consecutive positive integers is: {result}")
