import random
from hangman_art import stages, logo
from hangman_words import word_list

def play_hangman():
    """
    Play the classic Hangman game.

    In this game, the computer randomly selects a word from a predefined list,
    and the player attempts to guess the word by inputting one letter at a time.
    The player has a limited number of lives, and they win if they guess the word
    correctly before running out of lives. The game provides feedback and displays
    ASCII art for the hangman stages.

    Args:
        None

    Returns:
        None
    """

    print(logo)  # Display the logo at the start of the game
    game_is_finished = False  # Flag to track the game's status
    lives = len(stages) - 1  # Set the number of lives based on the hangman stages

    # Randomly select a word from the word list
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)

    # Create a display list to show the current state of guessed letters
    display = ["_"] * word_length  # Initialize display with underscores

    while not game_is_finished:
        guess = input("Guess a letter: ").lower()  # Get user input and convert to lowercase

        # Check if the letter has already been guessed
        if guess in display:
            print(f"You've already guessed '{guess}'.")
            continue  # Skip the rest of the loop if the letter was already guessed

        # Update the display with the guessed letter if it's in the chosen word
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter  # Reveal the letter in the display

        print(f"{' '.join(display)}")  # Show the current state of the word

        # Check if the guessed letter is not in the chosen word
        if guess not in chosen_word:
            print(f"You guessed '{guess}', that's not in the word. You lose a life.")
            lives -= 1  # Decrease the number of lives
            if lives == 0:
                game_is_finished = True  # End the game if no lives are left
                print("You lose. The word was:", chosen_word)

        # Check if the player has guessed all the letters
        if "_" not in display:
            game_is_finished = True  # End the game if the word is fully guessed
            print("You win! The word was:", chosen_word)

        print(stages[lives])  # Display the current hangman stage

# To start the game, call the play_hangman() function when the script is executed
if __name__ == "__main__":
    play_hangman()
