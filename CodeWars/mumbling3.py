def accum(s):
    """
    This function takes a string `s` and returns a new string where each character
    of `s` is repeated according to its position in the string (1-based index),
    with the first character in uppercase and the rest in lowercase. Each modified
    character sequence is joined by a hyphen.

    Parameters:
    s (str): The input string containing only letters from a..z and A..Z.

    Returns:
    str: The transformed string.

    Examples:
    accum("abcd") -> "A-Bb-Ccc-Dddd"
    accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
    accum("cwAt") -> "C-Ww-Aaa-Tttt"
    """
    # Enumerate over the string to get both the index and the character
    # For each character, create a new string where the character is repeated
    # according to its position (index + 1) with the first character in uppercase
    # and the rest in lowercase. Join these strings with a hyphen.
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))

# Driver code to test the function
if __name__ == "__main__":
    # Test cases
    print(accum("abcd"))  # Expected output: "A-Bb-Ccc-Dddd"
    print(accum("RqaEzty"))  # Expected output: "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
    print(accum("cwAt"))  # Expected output: "C-Ww-Aaa-Tttt"
    print(accum("ZpglnRxqenU"))  # Expected output: "Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu"
    print(accum("NyffsGeyylB"))  # Expected output: "N-Yy-Fff-Ffff-Sssss-Gggggg-Eeeeeee-Yyyyyyyy-Yyyyyyyyy-Llllllllll-Bbbbbbbbbbb"
