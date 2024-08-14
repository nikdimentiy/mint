from art import logo

# Define the alphabet as a dictionary for quick lookup
alphabet = {chr(i): i - 97 for i in range(97, 123)}  # a-z
reverse_alphabet = {i - 97: chr(i) for i in range(97, 123)}  # 0-25 to a-z

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
            position = alphabet[char]
            new_position = (position + shift_amount) % 26  # Wrap around using modulo
            end_text += reverse_alphabet[new_position]
        else:
            end_text += char  # Keep non-alphabet characters unchanged

    print(f"Here's the {cipher_direction}d result: {end_text}")

def main():
    print(logo)
    should_end = False

    while not should_end:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        if direction not in ['encode', 'decode']:
            print("Invalid option. Please type 'encode' or 'decode'.")
            continue

        text = input("Type your message:\n").lower()
        try:
            shift = int(input("Type the shift number:\n"))
        except ValueError:
            print("Please enter a valid number for the shift.")
            continue

        shift = shift % 26  # Ensure the shift value is within the range [0, 25]
        caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

        restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
        if restart == "no":
            should_end = True
            print("Goodbye")

if __name__ == "__main__":
    main()
