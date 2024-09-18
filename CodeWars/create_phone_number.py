def create_phone_number(n):
    """
    Convert an array of 10 integers (0-9) into a formatted phone number string.

    Args:
    n (list of int): A list containing exactly 10 integers, each between 0 and 9.

    Returns:
    str: A string representing the phone number in the format "(XXX) XXX-XXXX".
    """
    # Extract the first three digits for the area code
    str1 = ''.join(str(x) for x in n[0:3])
    # Extract the next three digits for the central office code
    str2 = ''.join(str(x) for x in n[3:6])
    # Extract the last four digits for the line number
    str3 = ''.join(str(x) for x in n[6:10])

    # Format and return the phone number
    return '({}) {}-{}'.format(str1, str2, str3)

# Driver code to test the function
if __name__ == "__main__":
    # Test case
    phone_number = create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
    print(phone_number)  # Expected output: "(123) 456-7890"
