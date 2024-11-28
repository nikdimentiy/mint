def accum(s):
    """
    Transform a string such that each character is followed by itself repeated 
    a number of times equal to its position in the string (0-indexed), 
    with the first character capitalized and the rest in lowercase. 
    Each transformed character sequence is separated by a hyphen.

    Parameters:
    s (str): The input string containing only letters from a..z and A..Z.

    Returns:
    str: The transformed string with the specified format.
    """
    # Create a list comprehension to build the transformed parts of the string
    # For each character in the string, capitalize it and repeat it based on its index
    return "-".join([s[i].upper() + (s[i].lower() * i) for i in range(len(s))])

# Driver code to test the accum function
if __name__ == "__main__":
    # Test cases
    print(accum("abcd"))      # Expected output: "A-Bb-Ccc-Dddd"
    print(accum("RqaEzty"))   # Expected output: "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
    print(accum("cwAt"))      # Expected output: "C-Ww-Aaa-Tttt"
