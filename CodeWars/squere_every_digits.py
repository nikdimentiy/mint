def square_digits(num):
    """
    This function takes an integer 'num' as input, squares each of its digits,
    and returns a new integer formed by concatenating the squared digits.

    Parameters:
    num (int): The integer whose digits are to be squared.

    Returns:
    int: An integer formed by concatenating the squared digits of 'num'.
    """
    # Convert the number to a string to iterate over each digit
    # Square each digit and convert it back to a string
    squared_digits = [str(int(n) ** 2) for n in str(num)]
    
    # Join the squared digits into a single string and convert it back to an integer
    return int("".join(squared_digits))

# Driver code to test the function
if __name__ == "__main__":
    # Test cases
    test_numbers = [9119, 123, 0, 45]
    
    for number in test_numbers:
        result = square_digits(number)
        print(f"The squared digits of {number} is {result}")
