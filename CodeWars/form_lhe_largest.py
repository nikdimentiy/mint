def max_number(n):
    """
    Returns the maximum number that can be formed from the digits of the given natural number.

    Parameters:
    n (int): A natural number whose digits will be rearranged.

    Returns:
    int: The maximum number formed by rearranging the digits of n.
    
    Example:
    >>> max_number(2736)
    7632
    >>> max_number(42145)
    54421
    """
    # Convert the number to a string to access its digits
    # Create a list of digits from the string representation of the number
    # Sort the digits in descending order to form the largest possible number
    # Join the sorted digits back into a string and convert it to an integer
    return int("".join(sorted([i for i in str(n)], reverse=True)))

# Driver code to test the function
if __name__ == "__main__":
    # Test cases
    print(max_number(2736))  # Output: 7632
    print(max_number(42145)) # Output: 54421
    print(max_number(9876543210)) # Output: 9876543210
    print(max_number(1001))  # Output: 1100
    print(max_number(0))     # Output: 0 (though 0 is not a natural number, it's included for completeness)
