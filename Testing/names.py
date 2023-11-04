from name_function import get_formatted_name

# This script takes user input for first and last names and formats them into a full name.

# Display a message to the user, explaining how to quit.
print("Enter 'q' at any time to quit.")

while True:
    try:
        # Prompt the user for a first name.
        first = input("\nPlease give me a first name:")
        
        # Check if the user wants to quit (by entering 'q').
        if first == 'q':
            break

        # Prompt the user for a last name.
        last = input("Please give me a last name: ")

        # Check if the user wants to quit (by entering 'q').
        if last == 'q':
            break

        # Call the get_formatted_name function to format the full name.
        formatted_name = get_formatted_name(first, last)

        # Display the neatly formatted name to the user.
        print("\tNeatly formatted name: " + formatted_name + ".")
    
    except Exception as e:
        # Handle any exceptions that may occur, e.g., invalid input.
        print(f"An error occurred: {e}")

# End of the while loop. The program exits when the user enters 'q' at any time.
