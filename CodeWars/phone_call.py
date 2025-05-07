def solution(min1, min2_10, min11, s):
    """
    Calculate the maximum duration of a phone call in minutes based on the given pricing structure.

    Parameters:
    min1 (int): Cost in cents for the first minute of the call.
    min2_10 (int): Cost in cents for each minute from the 2nd to the 10th minute (inclusive).
    min11 (int): Cost in cents for each minute after the 10th minute.
    s (int): Total amount in cents available on the account before the call.

    Returns:
    int: The maximum duration of the call in minutes, rounded down to the nearest integer.
    """
    
    # Check if the account balance is less than the cost of the first minute
    if s < min1:
        return 0  # Cannot make any call

    # Deduct the cost of the first minute from the balance
    remaining_balance = s - min1

    # Check if the remaining balance can cover the cost of minutes 2 to 10
    if remaining_balance < min2_10 * 9:
        return 1 + remaining_balance // min2_10  # Return total minutes including the first minute

    # Deduct the cost for minutes 2 to 10 (9 minutes)
    remaining_balance -= min2_10 * 9
    
    # Calculate the number of minutes that can be covered after the 10th minute
    return 10 + remaining_balance // min11  # Return total minutes including the first 10 minutes


# Driver code to test the solution
if __name__ == "__main__":
    # Test cases
    print(solution(3, 2, 5, 20))  # Expected output: 10
    print(solution(2, 3, 1, 10))  # Expected output: 4
    print(solution(5, 2, 1, 5))   # Expected output: 1
    print(solution(1, 1, 1, 0))    # Expected output: 0
    print(solution(1, 2, 3, 30))   # Expected output: 20
