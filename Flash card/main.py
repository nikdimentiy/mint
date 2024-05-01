from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"  # Background color for the app
current_card = {}  # Dictionary to store the current flashcard data
to_learn = {}  # Dictionary to store the words left to learn

# Load data from a CSV file, or initialize if it doesn't exist
def load_data():
    """
    Load word data from a CSV file.
    If 'words_to_learn.csv' exists, load it. Otherwise, load 'french_words.csv'.
    """
    global to_learn
    try:
        # Try loading data from the saved CSV file
        data = pandas.read_csv("data/words_to_learn.csv")
    except FileNotFoundError:
        # If not found, load from the original data source
        original_data = pandas.read_csv("data/french_words.csv")
        to_learn = original_data.to_dict(orient="records")
    else:
        # If found, convert data to a list of dictionaries
        to_learn = data.to_dict(orient="records")

# Flip the flashcard to reveal the translation
def flip_card():
    """
    Flip the flashcard to show the English translation.
    Changes the displayed image and text to represent the 'flipped' state.
    """
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

# Display the next card in the set
def next_card():
    """
    Display the next flashcard. Selects a random card from 'to_learn',
    sets the text and background image, and schedules a flip after 3 seconds.
    """
    global current_card, flip_timer
    # Cancel the existing flip timer
    window.after_cancel(flip_timer)
    # Select a random card and display the French word
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    # Schedule a flip after 3 seconds
    flip_timer = window.after(3000, func=flip_card)

# Mark the current card as 'known' and save the updated set to the CSV file
def is_known():
    """
    Mark the current card as 'known', remove it from 'to_learn',
    and update 'words_to_learn.csv' with the reduced set.
    """
    # Remove the current card from the learning set
    to_learn.remove(current_card)
    # Save the updated set to the CSV file
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    # Move to the next card
    next_card()

# Main UI setup
def create_flashcard_ui():
    """
    Create the flashcard UI with buttons and display elements.
    """
    global card_front_img, card_back_img, card_background
    global card_title, card_word, flip_timer
    
    # Create the main application window
    window = Tk()
    window.title("Flashy")
    window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
    
    # Set up the flip timer
    flip_timer = window.after(3000, func=flip_card)
    
    # Create a canvas for the flashcards
    canvas = Canvas(window, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
    card_front_img = PhotoImage(file="images/card_front.png")
    card_back_img = PhotoImage(file="images/card_back.png")
    card_background = canvas.create_image(400, 263, image=card_front_img)
    card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
    card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
    canvas.grid(row=0, column=0, columnspan=2)
    
    # Create the 'unknown' button (to skip to the next card)
    cross_image = PhotoImage(file="images/wrong.png")
    unknown_button = Button(window, image=cross_image, highlightthickness=0, command=next_card)
    unknown_button.grid(row=1, column=0)
    
    # Create the 'known' button (to mark the current card as learned)
    check_image = PhotoImage(file="images/right.png")
    known_button = Button(window, image=check_image, highlightthickness=0, command=is_known)
    known_button.grid(row=1, column=1)
    
    # Display the first card
    next_card()
    
    # Start the Tkinter main loop
    window.mainloop()

# Load the data and create the flashcard UI
load_data()
create_flashcard_ui()
