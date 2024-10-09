def solution(cipher):
    """
    Decodes a list of integers representing ASCII values into a string.
    
    The function takes a list of integers (cipher) where each integer is a digit (0-9).
    It constructs numbers from these digits and converts them to characters if the 
    constructed number is greater than or equal to 97 (ASCII value for 'a').
    
    Args:
        cipher (iterable): An iterable of integers (0-9) representing the cipher.
        
    Returns:
        str: The decoded string formed by characters corresponding to ASCII values 
             greater than or equal to 97.
    """
    # Convert the input iterable to a list of integers
    arr = list(map(int, cipher))
    curr = 0  # Current number being constructed from digits
    ret = []   # List to hold the resulting characters

    # Iterate through each number in the array
    for num in arr:
        # Construct the current number by shifting left and adding the new digit
        curr = curr * 10 + num
        
        # If the constructed number is a valid ASCII value for a character
        if curr >= 97:
            # Append the corresponding character to the result list
            ret.append(chr(curr))
            # Reset the current number for the next iteration
            curr = 0
            
    # Join the list of characters into a single string and return it
    return ''.join(ret)

# Driver code to test the solution function
if __name__ == "__main__":
    # Example input: a list of digits that can form ASCII values
    cipher_input = [1, 0, 9, 7, 1, 0, 9, 8, 1, 0, 9, 9]
    # Call the solution function with the example input
    decoded_string = solution(cipher_input)
    # Print the result
    print(f"Decoded string: {decoded_string}")
