# ➡️ Python password manager application with a Tkinter-based GUI, 🎯
# ➡️ that empowers users to effortlessly generate robust passwords, 🍀
# ➡️ securely store them for various websites, and effortlessly search for passwords associated with specific websites. 🕸️

from tkinter import * 
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip # pip install pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Function to generate a random password
def generate_password():
    # Lists of characters to use in the password
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Randomly select characters for the password
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    # Combine and shuffle the characters to create the password
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    # Convert the password list to a string
    password = "".join(password_list)

    # Display the password in the entry field and copy it to the clipboard
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # Get user input from the entry fields
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    # Create a dictionary to store the new data
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    # Check if any field is empty and show an error message if so
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            # Attempt to open the data file for reading
            with open("data.json", "r") as data_file:
                # Read the existing data from the file
                data = json.load(data_file)
        except FileNotFoundError:
            # If the file doesn't exist, create it and write the new data
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # If the file exists, update it with the new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # Save the updated data to the file
                json.dump(data, data_file, indent=4)
        finally:
            # Clear the entry fields after saving
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    # Get the website name from the entry field
    website = website_entry.get()
    try:
        # Attempt to open the data file for reading
        with open("data.json") as data_file:
            # Read the data from the file
            data = json.load(data_file)
    except FileNotFoundError:
        # Show an error message if the file doesn't exist
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        # Check if the website exists in the data dictionary
        if website in data:
            # If found, retrieve the email and password and display them
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            # If not found, show an error message
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

# ---------------------------- UI SETUP ------------------------------- #

# Create the main application window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Create a canvas for the logo
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels for entry fields
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entry fields for website, email, and password
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "nikdimentiy@yahoo.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons for searching, generating passwords, and saving data
search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(row=1, column=2)
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

# Start the main application loop
window.mainloop()

