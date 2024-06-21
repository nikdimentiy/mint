from tkinter import Tk, Label, Entry, Button

"""
Miles to Kilometer Converter

This program creates a simple GUI application that converts miles to kilometers.
The user inputs a value in miles, and upon clicking the "Calculate" button, the 
equivalent value in kilometers is displayed.

Improvements:
- Added better spacing and padding for improved layout.
- Added an initial focus on the entry widget for better user experience.
"""

def miles_to_km():
    """
    Converts the value from miles to kilometers and updates the result label.
    """
    try:
        miles = float(miles_input.get())
        km = round(miles * 1.609, 3)
        kilometer_result_label.config(text=f"{km}")
    except ValueError:
        kilometer_result_label.config(text="Invalid input")

# Initialize the main window
window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

# Entry widget to accept miles input
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)
miles_input.focus()  # Set focus on the entry widget for better UX

# Label for the miles input
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# Label for the conversion text
is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

# Label to display the result in kilometers
kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

# Label for the kilometers text
kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

# Button to trigger the conversion
calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

# Start the main event loop
window.mainloop()
