def hex_hash(s):
    """
    Calculate the sum of the numeric values in the hexadecimal representation 
    of the ASCII codes of characters in a string.

    Args:
        s (str): The input string.

    Returns:
        int: The sum of all numeric values found in the hexadecimal representation 
             of the ASCII values of the characters in the input string.
    """
    # Iterate over each character in the string `s`
    return sum(
        # Sum the numeric digits in the hexadecimal representation of each character's ASCII value
        sum(int(c) for c in hex(ord(c))[2:] if c in "0123456789") 
        for c in s
    )

# Driver code
if __name__ == "__main__":
    # Test cases
    test_cases = [
        ("abc", "Expected: 12 (hex: 61, 62, 63 -> 6+1+6+2+6+3)"),
        ("123", "Expected: 6 (hex: 31, 32, 33 -> 3+1+3+2+3+3)"),
        ("!@#", "Expected: 1 (hex: 21, 40, 23 -> 2+1)"),
        ("", "Expected: 0 (empty string)"),
    ]

    for string, description in test_cases:
        result = hex_hash(string)
        print(f"Input: '{string}' | Output: {result} | {description}")
