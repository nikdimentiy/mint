"""
This program prompts the user to enter a string, then checks if the string starts with 'i', ends with 'n', and contains 'a'.
The program is case-insensitive and prints "Found!" if the conditions are met, and "Not Found!" otherwise.
"""

# Prompt the user to enter a string
string = input("Enter a string: ")
# Convert the string to lower-case
string = string.lower()
# Check if the string starts with 'i', ends with 'n', and contains 'a'
if string.startswith("i") and string.endswith("n") and "a" in string:
    # Print "Found!" if the condition is true
    print("Found!")
else:
    # Print "Not Found!" otherwise
    print("Not Found!")
