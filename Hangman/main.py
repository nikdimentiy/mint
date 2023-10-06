import random
from hangman_art import stages, logo
from hangman_words import word_list

def play_hangman():
    """
    This function allows two or more players to play the classic hangman game with the computer.
    The computer selects a random word from a predefined list, and the player(s) attempt to guess the word
    by inputting one letter at a time. Players have a limited number of lives, and they win if they guess
    the word correctly before running out of lives or lose if they exhaust all their lives.

    The game uses ASCII art for displaying hangman stages and provides feedback to the players as they play.

    Args:
        None

    Returns:
        None
    """

    print(logo)
    game_is_finished = False
    lives = len(stages) - 1

    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)

    display = []
    for _ in range(word_length):
        display += "_"

    while not game_is_finished:
        guess = input("Guess a letter: ").lower()

        if guess in display:
            print(f"You've already guessed {guess}")

        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
        print(f"{' '.join(display)}")

        if guess not in chosen_word:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            lives -= 1
            if lives == 0:
                game_is_finished = True
                print("You lose.")

        if "_" not in display:
            game_is_finished = True
            print("You win.")

        print(stages[lives])

# To start the game, you can call the play_hangman() function.
if __name__ == "__main__":
    play_hangman()
