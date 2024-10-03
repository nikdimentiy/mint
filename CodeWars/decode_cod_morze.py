def decodeMorse(morse_code):
    """
    Decodes a given Morse code string into a human-readable message.

    Args:
        morse_code (str): A string containing Morse code, where each letter is separated by a space
                          and words are separated by two spaces.

    Returns:
        str: The decoded message in plain text.
    """
    # Split the morse_code string into individual Morse code symbols
    # and decode each symbol into its corresponding character
    message = "".join(
        [morse_code[i] if i in morse_code else " " for i in morse_code.split(" ")]
    )
    
    # Replace multiple spaces with a single space and strip leading/trailing spaces
    return message.replace("  ", " ").strip()

# Driver code to test the decodeMorse function
if __name__ == "__main__":
    # Example Morse code input
    morse_code_input = "... --- ..."
    
    # Decode the Morse code
    decoded_message = decodeMorse(morse_code_input)
    
    # Print the decoded message
    print(f"Decoded Message: '{decoded_message}'")
