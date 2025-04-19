def limit(num):
    """
    Limit a number to be within the range of 0 to 255.

    If the number is less than 0, it returns 0.
    If the number is greater than 255, it returns 255.
    Otherwise, it returns the number itself.

    Parameters:
    num (int): The input number to be limited.

    Returns:
    int: The limited number, which will be between 0 and 255.
    """
    if num < 0:
        return 0  # Return 0 if the number is less than 0
    if num > 255:
        return 255  # Return 255 if the number is greater than 255
    return num  # Return the number itself if it's within the range


def rgb(r, g, b):
    """
    Convert RGB values to a hexadecimal color string.

    Each RGB component (r, g, b) is limited to the range of 0 to 255
    using the `limit` function, and then formatted as a two-digit
    hexadecimal string.

    Parameters:
    r (int): The red component of the color.
    g (int): The green component of the color.
    b (int): The blue component of the color.

    Returns:
    str: A string representing the color in hexadecimal format (e.g., "FF00FF").
    """
    return "{:02X}{:02X}{:02X}".format(limit(r), limit(g), limit(b))


# Driver code to test the functions
if __name__ == "__main__":
    # Test cases for the rgb function
    print(rgb(255, 0, 0))    # Expected output: "FF0000" (Red)
    print(rgb(0, 255, 0))    # Expected output: "00FF00" (Green)
    print(rgb(0, 0, 255))    # Expected output: "0000FF" (Blue)
    print(rgb(255, 255, 255))  # Expected output: "FFFFFF" (White)
    print(rgb(0, 0, 0))      # Expected output: "000000" (Black)
    print(rgb(256, 100, -20))  # Expected output: "FF0064" (Limits applied)
