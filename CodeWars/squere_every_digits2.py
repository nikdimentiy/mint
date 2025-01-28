def square_digits(num):
    """
    Squares each digit of the input number and concatenates the results.

    Args:
        num (int): The number whose digits are to be squared.

    Returns:
        int: The resulting number after squaring and concatenating each digit.
    """
    ret = ""  # Initialize an empty string to store the squared digits
    for x in str(num):  # Convert the number to a string to iterate through each digit
        ret += str(int(x) ** 2)  # Square the digit and append it to the result string
    return int(ret)  # Convert the result string back to an integer and return it

# Driver code
if __name__ == "__main__":
    # Test cases
    print(square_digits(9119))  # Output: 811181
    print(square_digits(123))   # Output: 149
    print(square_digits(0))     # Output: 0
