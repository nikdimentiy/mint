def computer_to_phone(input_str):
    """
    Convert a string of computer keypad numbers to their corresponding phone keypad numbers.

    The mapping is based on the layout of a standard computer keyboard and a traditional phone keypad.
    For example, the computer number '7' corresponds to '1' on the phone keypad.

    Parameters:
    input_str (str): A string containing digits from a computer keypad.

    Returns:
    str: A string representing the corresponding phone keypad numbers.
    """
    
    # Define a dictionary that maps computer keypad numbers to phone keypad numbers
    mapping = {
        "0": "0",
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "1",  # Computer '7' maps to Phone '1'
        "8": "2",  # Computer '8' maps to Phone '2'
        "9": "3",  # Computer '9' maps to Phone '3'
    }
    
    # Initialize an empty string to store the converted phone number
    phone_str = ""
    
    # Convert each character in the input string using the mapping dictionary
    for char in input_str:
        phone_str += mapping[char]  # Append the mapped value to phone_str
    
    return phone_str

# Driver code to test the function
if __name__ == "__main__":
    # Test cases
    test_cases = [
        "1234567890",  # Expected output: "1234567890"
        "9876543210",  # Expected output: "3216549870"
        "000",         # Expected output: "000"
        "123",         # Expected output: "123"
        "789",         # Expected output: "123"
    ]
    
    for test in test_cases:
        result = computer_to_phone(test)
        print(f"Input: {test} => Output: {result}")
