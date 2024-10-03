# Define the Morse code dictionary
MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
    '8': '---..', '9': '----.', '0': '-----', ' ': '/'
}

def decodeMorse(morse_sequence):
    """
    Decodes a Morse code sequence into human-readable text.

    Args:
        morse_sequence (str): A string containing Morse code, where 
                              words are separated by three spaces and 
                              letters are separated by a single space.

    Returns:
        str: The decoded human-readable text.
    """
    words = []  # List to hold decoded words
    # Split the Morse sequence into words based on three spaces
    for morse_word in morse_sequence.split('   '):
        # Decode each Morse word into letters
        word = ''.join(MORSE_CODE.get(morse_char, '') 
                       for morse_char in morse_word.split(' '))
        if word:  # Only add non-empty words
            words.append(word)
    # Join the decoded words with a space and return
    return ' '.join(words)

# Driver code to test the decodeMorse function
if __name__ == "__main__":
    # Example Morse code sequence
    morse_input = "... --- ...   .... . .-.. .-.. ---"
    decoded_message = decodeMorse(morse_input)
    print(f"Decoded Message: {decoded_message}")  # Output: "SOS HELLO"
