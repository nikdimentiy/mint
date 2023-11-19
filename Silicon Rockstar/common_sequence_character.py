"""
This program takes a string as input and finds the most common character in the string
along with the number of occurrences of that character.
"""

# Get user input
my_string = input("Enter some string sequence: ")

# Initialize variables and data structures
answer = ""           # Variable to store the most common character
answer_count = 0      # Variable to store the count of the most common character
my_dictionary = {}    # Dictionary to store character occurrences

# Compute character occurrences
for now in my_string:
    if now not in my_dictionary:
        my_dictionary[now] = 0
    my_dictionary[now] += 1

# Find the most common character and its count
for key in my_dictionary:
    if my_dictionary[key] > answer_count:
        answer_count = my_dictionary[key]
        answer = key

# Output the result
print(f"The most common sequence character is: {answer}")  # Big O notation = O(n)
print(f"The number of occurrences of this symbol in the sequence is: {answer_count}")
