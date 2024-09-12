def filter_string(st: str) -> int:
    """
    Filter out non-digit characters from a string and return the result as an integer.

    Args:
    st (str): The input string to filter.

    Returns:
    int: The integer formed by the digits in the input string.
         Returns 0 if no digits are found.

    Example:
    >>> filter_string("a1b2c3")
    123
    >>> filter_string("abc")
    0
    """
    result = ""  # Initialize an empty string to store the digits
    for char in st:  # Iterate through each character in the input string
        if char.isdigit():  # Check if the character is a digit
            result += char  # Append the digit to the result string
    return (
        int(result) if result else 0
    )  # Convert to int and return, or return 0 if no digits found


# Driver code
if __name__ == "__main__":
    # Test cases
    test_cases = [
        "123",
        "1123",
        "112233",
        "abc",
        "a1b2c3",
        "100a200b300",
        "",
        "0",
    ]

    print("Testing filter_string function:")
    for test in test_cases:
        result = filter_string(test)
        print(f"Input: '{test}' -> Output: {result}")

    # Additional test to demonstrate usage
    user_input = input("\nEnter a string to filter: ")
    filtered_result = filter_string(user_input)
    print(f"Filtered result: {filtered_result}")
