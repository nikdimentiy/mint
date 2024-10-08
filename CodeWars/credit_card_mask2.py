def maskify(cc):
    """
    Mask all but the last four characters of a credit card number.

    Parameters:
    cc (str): The credit card number as a string.

    Returns:
    str: A masked version of the credit card number, where all but the last four characters are replaced with '#'.
    """
    # Get the length of the credit card number
    l = len(cc)
    
    # If the length is 4 or less, return the original credit card number
    if l <= 4:
        return cc
    
    # Mask all but the last four characters with '#'
    return (l - 4) * '#' + cc[-4:]

# Driver code to test the maskify function
if __name__ == "__main__":
    # Test cases
    print(maskify("1234567890123456"))  # Output: "############3456"
    print(maskify("1234"))               # Output: "1234"
    print(maskify("123"))                # Output: "123"
    print(maskify("1"))                  # Output: "1"
    print(maskify(""))                   # Output: ""
