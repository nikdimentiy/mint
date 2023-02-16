# Coursera assignment --> coding: snippets in Python, Java, Go

#  Write a program which prompts the user to enter a string. The program searches through the entered string for the characters ‘i’, ‘a’, and ‘n’.
#  The program should print “Found!” if the entered string starts with the character ‘i’, ends with the character ‘n’, and contains the character ‘a’.
#  The program should print “Not Found!” otherwise. The program should not be case-sensitive, so it does not matter if the characters are upper-case or lower-case.

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
