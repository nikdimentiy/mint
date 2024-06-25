import pandas as pd

# Read the data from a CSV file named "nato_phonetic_alphabet.csv" into a pandas DataFrame.
try:
    data = pd.read_csv("nato_phonetic_alphabet.csv")
except FileNotFoundError:
    print("The CSV file was not found.")
    exit()

# Create a dictionary that maps letters to their corresponding NATO phonetic codes.
phonetic_dict = {row.letter: row.code for _, row in data.iterrows()}

# Print the phonetic_dict to display the mapping of letters to codes.
print(phonetic_dict)

# Define a function named generate_phonetic.
def generate_phonetic():
    while True:
        # Prompt the user to enter a word and convert it to uppercase for consistency.
        word = input("Enter a word: ").upper()
        
        # Check if the word contains only alphabetic characters.
        if not word.isalpha():
            print("Sorry, only letters in the alphabet please.")
            continue
        
        # Create an output_list by looking up the phonetic code for each letter in the input word.
        output_list = [phonetic_dict[letter] for letter in word]
        # Print the list of NATO phonetic codes for the input word.
        print(output_list)
        break

# Call the generate_phonetic function to start the program.
generate_phonetic()
