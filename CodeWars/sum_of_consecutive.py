def solution(n):
    """
    Counts the number of ways to express a positive integer n as a sum of consecutive positive integers.

    Parameters:
    n (int): The positive integer to be expressed as a sum.

    Returns:
    int: The number of ways to express n as a sum of consecutive positive integers.
    """

    start, end = 1, 1  # initialize start and end variables to 1
    sum = 1  # initialize sum variable to 1
    count = 0  # initialize count variable to 0

    while start < n:  # loop until start reaches n
        if sum == n:  # if the sum is equal to n
            count += 1  # increment the count by 1
            sum -= start  # subtract the start from the sum
            start += 1  # increment the start by 1
        elif sum < n:  # if the sum is less than n
            end += 1  # increment the end by 1
            sum += end  # add the end to the sum
        else:  # if the sum is greater than n
            sum -= start  # subtract the start from the sum
            start += 1  # increment the start by 1

    return count  # return the final count
