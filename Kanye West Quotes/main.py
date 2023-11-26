from tkinter import *
import requests

def get_quote():
    """
    Function to fetch a Kanye West quote from the Kanye.rest API and update the canvas with the quote.
    """
    # Send a GET request to the Kanye.rest API
    response = requests.get("https://api.kanye.rest")
    
    # Raise an exception if the request was unsuccessful
    response.raise_for_status()
    
    # Parse the JSON response
    data = response.json()
    
    # Extract the quote from the data
    quote = data["quote"]
    
    # Update the canvas with the new quote
    canvas.itemconfig(quote_text, text=quote)

# Create the main window
window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

# Create a canvas for displaying the background image and the Kanye quote
canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)

# Create a text element for displaying the Kanye quote
quote_text = canvas.create_text(
    150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white"
)
canvas.grid(row=0, column=0)

# Load the Kanye image and create a button to fetch a new quote
kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

# Start the Tkinter event loop
window.mainloop()

