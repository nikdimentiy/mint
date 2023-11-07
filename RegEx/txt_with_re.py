import re  # Import the regular expression module to perform pattern matching.

# Define the name of the input file to read from.
file_name = "fw.txt"

# Open the specified file for reading using a context manager to ensure it's properly closed when done.
with open(file_name) as file_obj:
    # Read all the lines from the file and store them in a list.
    lines = file_obj.readlines()
    common_string = ""  # Initialize an empty string to store the concatenated content of the file.

    # Loop through each line in the file.
    for line in lines:
        common_string += line.strip()  # Remove leading/trailing whitespaces and concatenate the lines.

# Define a regular expression pattern to match digits (0-9).
pattern = r'[0-9]'

# Use the regular expression module to substitute all matched digits in the common_string with an empty string ('').
new_string = re.sub(pattern, '', common_string)

# Open a new file, "frequently_english_words.txt," for writing, using a context manager.
with open("frequently_english_words.txt", 'w') as file_obj:
    # Write the modified (digit-removed) content to the new file.
    file_obj.write(new_string)
