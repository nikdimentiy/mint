import json

filename = 'numbers.json'

# Open the JSON file in read mode using a with statement
with open(filename) as f_obj:
    # Load the JSON data from the file into a Python data structure
    numbers = json.load(f_obj)

# Print the loaded data
print(numbers)
