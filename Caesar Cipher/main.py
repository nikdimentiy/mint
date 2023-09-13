# Import the logo from the 'art' module
from art import logo

# Define the alphabet as a list for reference
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Define a function to perform the Caesar cipher
def caesar(start_text, shift_amount, cipher_direction):
    """
    Encrypts or decrypts a message using the Caesar cipher.

    :param start_text: The text to be encrypted or decrypted.
    :param shift_amount: The number of positions to shift the letters in the alphabet.
    :param cipher_direction: Either 'encode' to encrypt or 'decode' to decrypt.
    :return: The result of the encryption or decryption.
    """
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Here's the {cipher_direction}d result: {end_text}")

# Display the program logo
print(logo)

# Initialize a variable to control the loop
should_end = False

# Main program loop
while not should_end:
    # Get user input for the encryption/decryption operation
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # Ensure the shift value is within the range [0, 25]
    shift = shift % 26

    # Call the caesar function to perform the operation
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    # Ask the user if they want to repeat the process
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")
