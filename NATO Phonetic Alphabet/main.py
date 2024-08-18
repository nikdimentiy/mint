import pandas

# Load the NATO phonetic alphabet data from a CSV file
data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Create a dictionary mapping each letter to its corresponding phonetic code
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

def generate_phonetic():
    """
    Generates the NATO phonetic alphabet representation of a given word.
    
    The function prompts the user to enter a word, converts it to uppercase,
    and then translates each letter into its corresponding phonetic code
    using the phonetic_dict. If the user enters a non-alphabetic character,
    an error message is displayed, and the user is prompted to enter a word
    again.
    """
    word = input("Enter a word: ").upper()  # Get user input and convert to uppercase
    try:
        # Create a list of phonetic codes for each letter in the word
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        # Handle the case where a non-alphabetic character is entered
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()  # Recursively call the function to prompt again
    else:
        # Print the resulting list of phonetic codes
        print(output_list)

# Driver code to execute the function
if __name__ == "__main__":
    generate_phonetic()
