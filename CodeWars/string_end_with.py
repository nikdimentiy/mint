def solution(string, ending):
    """
    Check if the given string ends with the specified ending string.

    Args:
    string (str): The main string to check.
    ending (str): The string to check if it is the ending of the main string.

    Returns:
    bool: True if the main string ends with the ending string, False otherwise.
    """
    # Use the built-in str.endswith() method to check if 'string' ends with 'ending'
    return string.endswith(ending)

# Driver code to test the solution function
if __name__ == "__main__":
    # Test cases
    print(solution('abc', 'bc'))  # Expected output: True
    print(solution('abc', 'd'))   # Expected output: False
    print(solution('hello', 'lo')) # Expected output: True
    print(solution('hello', 'hello')) # Expected output: True
    print(solution('hello', 'Hello')) # Expected output: False
