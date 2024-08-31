def maskify(cc):
    """
    Mask all but the last four characters of a credit card number.

    This function takes a string representing a credit card number and replaces
    all characters except for the last four with the '#' character. This is useful
    for displaying credit card information securely, ensuring that sensitive data
    is not fully visible.

    Parameters:
    cc (str): The credit card number as a string.

    Returns:
    str: A masked version of the credit card number, with all but the last four
         characters replaced by '#'.
    """
    # Calculate the number of characters to mask
    num_to_mask = len(cc) - 4
    
    # Create the masked part and concatenate it with the last four characters
    return (num_to_mask * "#") + cc[-4:]

# Driver code to test the maskify function
if __name__ == "__main__":
    # Test cases
    test_cases = [
        "1234567890123456",  # Standard case
        "1234",              # Edge case: exactly 4 characters
        "123456",            # Edge case: 6 characters
        "123",               # Edge case: less than 4 characters
        "",                  # Edge case: empty string
        "abcd1234"          # Alphanumeric case
    ]

    for cc in test_cases:
        masked = maskify(cc)
        print(f"Original: {cc} -> Masked: {masked}")
