def find_most_frequent_character(s):
    """
    This function takes a string as input, iterates through its characters, and finds the most frequent character.
    
    Parameters:
    s (str): The input string
    
    Returns:
    tuple: A tuple containing the most frequent character and its count
    """

    # Initialize variables
    most_frequent_char = ""
    most_frequent_count = 0
    char_counts = {}

    # Iterate through the characters in the input string
    for char in s:
        # Update the character count in the dictionary
        char_counts[char] = char_counts.get(char, 0) + 1

        # Check if the current character has a higher count
        if char_counts[char] > most_frequent_count:
            most_frequent_char = char
            most_frequent_count = char_counts[char]

    # Print the result
    print("The most frequent character is:", most_frequent_char, "-> appearing", most_frequent_count, "times.")

# Test the function
input_string = input("Enter a string: ")
find_most_frequent_character(input_string)
