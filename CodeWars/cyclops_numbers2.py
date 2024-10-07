def cyclops(n):
    """
    Determine if a given positive integer is a cyclops number in binary representation.

    A cyclops number is defined as a binary number that consists of all 1's with exactly one 0 
    in the exact middle position. Cyclops numbers must have an odd number of digits.

    Parameters:
    n (int): A positive integer in decimal format.

    Returns:
    bool: True if the number is a cyclops number in binary, False otherwise.
    """
    # Convert the decimal number to binary and remove the '0b' prefix
    n = bin(n)[2:]

    # Check if there is exactly one '0' and if the binary representation is a palindrome
    return n.count("0") == 1 and n == n[::-1]

# Driver code to test the cyclops function
if __name__ == "__main__":
    test_numbers = [5, 7, 21, 15, 63, 73]  # 5 (101), 7 (111), 21 (10101), 15 (1111), 63 (111111), 73 (1001001)
    
    for number in test_numbers:
        result = cyclops(number)
        print(f"{number} is a cyclops number: {result}")
