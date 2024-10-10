def create_phone_number(n):
    """
    Convert an array of 10 integers (between 0 and 9) into a formatted phone number string.

    Args:
    n (list of int): A list containing exactly 10 integers, each between 0 and 9.

    Returns:
    str: A string representing the phone number in the format "(XXX) XXX-XXXX".
    """
    # Join the integers in the list into a single string
    s = "".join([str(i) for i in n])
    
    # Format the string into the desired phone number format
    return f"({s[:3]}) {s[3:6]}-{s[6:]}"

# Driver code to test the function
if __name__ == "__main__":
    # Test case
    phone_number = create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
    print(phone_number)  # Expected output: "(123) 456-7890"

    # Additional test cases
    print(create_phone_number([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))  # Expected output: "(012) 345-6789"
    print(create_phone_number([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))  # Expected output: "(987) 654-3210"
    print(create_phone_number([5, 5, 5, 5, 5, 5, 5, 5, 5, 5]))  # Expected output: "(555) 555-5555"
