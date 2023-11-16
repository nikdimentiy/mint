import json

def read_and_print_numbers_from_json(filename='numbers.json'):
    """
    Read and print the content of a JSON file.

    Parameters:
    - filename (str): The name of the JSON file to read. Default is 'numbers.json'.
    """
    try:
        with open(filename) as f_obj:  # Open the file in read mode using a context manager
            numbers = json.load(f_obj)  # Load JSON data from the file into the 'numbers' variable
            print(numbers)  # Print the content of the 'numbers' variable
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")
    except json.JSONDecodeError:
        print(f"Error decoding JSON in '{filename}'. Please check the file format.")

# Call the function to execute the code
read_and_print_numbers_from_json()
