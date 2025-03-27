def computer_to_phone(numbers):
    """
    Translates computer number pad layout to phone number pad layout.
    
    This function swaps the positions of numbers on a computer keyboard's 
    number pad to match the layout of a telephone number pad. Specifically, 
    it exchanges the positions of the following numbers:
    1 <-> 7
    2 <-> 8
    3 <-> 9
    
    Args:
        numbers (str): A string of numbers to be translated
    
    Returns:
        str: The translated number string with positions swapped
    
    Example:
        >>> computer_to_phone("123")
        "789"
        >>> computer_to_phone("567")
        "345"
    """
    # Use str.maketrans to create a translation map
    # Swapping 1<->7, 2<->8, 3<->9
    return numbers.translate(str.maketrans('123789', '789123'))

# Driver code to demonstrate the function
if __name__ == "__main__":
    # Test cases
    print(computer_to_phone("123"))  # Should print "789"
    print(computer_to_phone("567"))  # Should print "345"
    print(computer_to_phone(""))     # Should print "" (empty string)
    print(computer_to_phone("4560"))  # Should print "4560" (unchanged middle numbers)
