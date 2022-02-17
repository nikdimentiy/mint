from name_function import get_formatted_name
"""This function asks for a username and return a neatly formatted form"""

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name:")
    if first == 'q':
        break
    last = input("Please gime me a last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print("\tNeatly formatted name: " + formatted_name + ".")
