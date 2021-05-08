# Caesar's code

alphabet = ("abcdefghijklmnopqrstuvwxyz!@#$%/") * 26
print("Enter the number of operation: ")
choice = int(input("Enter your choice: 1 - Encrypt the message, 2 - Decrypt the message: "))

if choice == 1:
    open_message = input("Enter the message you want to encrypt: ")
    key_for_encrypt = int(input("Enter the code number: (1 - 25) "))

    if key_for_encrypt == 26:
        print("You entered illegal code number!")
    else:
        open_message = open_message.lower()
        encrypt_message = ''

        for letter in open_message:
            position = alphabet.find(letter)
            new_position = position + key_for_encrypt
            if letter in alphabet:
                encrypt_message = encrypt_message + alphabet[new_position]
            else:
                encrypt_message = encrypt_message + letter

        print("Your encrypt message is: ", encrypt_message)


elif choice == 2:
    encrypt_message = input("Enter the message you want to decrypt: ")
    key_for_encrypt = int(input("Enter the correct code for decrypt message: "))
    decrypt_message = ''
    for encrypt_letter in encrypt_message:
        position = alphabet.find(encrypt_letter)
        new_position = position - key_for_encrypt
        if encrypt_letter in alphabet:
            decrypt_message = encrypt_message - alphabet[new_position]
        else:
            decrypt_message = encrypt_message - encrypt_letter

    print("Your decrypt message is: ", decrypt_message)
