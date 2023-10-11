# Define a function to get the user's name and call the 'hello' function
def main():
    name = input("What is your name: ?")  # Prompt the user for their name
    print(hello(name))  # Call the 'hello' function and print the result

# Define a function to greet a person with their name or default to "world"
def hello(name="world"):
    return f"Hello, {name}"  # Return a greeting message with the provided name

if __name__ == "__main__":  # Check if the script is being run as the main program
    main()  # Call the 'main' function if this script is the main program
