# Import the pandas library, which is used for data manipulation and analysis.
import pandas as pd

# Read the data from a CSV file named "nato_phonetic_alphabet.csv" into a pandas DataFrame.
data = pd.read_csv("nato_phonetic_alphabet.csv")

# Create a dictionary that maps letters to their corresponding NATO phonetic codes.
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# Print the phonetic_dict to display the mapping of letters to codes.
print(phonetic_dict)

# Define a function named generate_phonetic.
def generate_phonetic():
    # Prompt the user to enter a word and convert it to uppercase for consistency.
    word = input("Enter a word: ").upper()
    
    try:
        # Create an output_list by looking up the phonetic code for each letter in the input word.
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        # Handle the case where a non-alphabetical character is entered.
        print("Sorry, only letters in the alphabet please.")
        # Recursively call the generate_phonetic function to allow the user to try again.
        generate_phonetic()
    else:
        # Print the list of NATO phonetic codes for the input word.
        print(output_list)

# Call the generate_phonetic function to start the program.
generate_phonetic()
