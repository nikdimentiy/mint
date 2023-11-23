from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
    """
    Compares the user's guess to the actual answer and returns the number of turns remaining.

    Args:
        guess (int): The user's guess for the secret number.
        answer (int): The actual secret number.
        turns (int): The remaining number of guesses.

    Returns:
        int: The number of turns remaining.
    """
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")


# Function to set difficulty based on user input.
def set_difficulty():
    """
    Prompts the user to choose a difficulty level and returns the corresponding number of turns.

    Args:
        None

    Returns:
        int: The number of turns for the chosen difficulty level.
    """
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    """
    Runs the main gameplay loop for the number guessing game.

    Args:
        None

    Returns:
        None
    """
    print(logo)

    # Choose a random number between 1 and 100.
    print("\n")
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")  # DEBUG: Comment out for actual gameplay

    # Set the number of turns based on the chosen difficulty.
    turns = set_difficulty()

    # Repeat the guessing functionality until the user guesses correctly or runs out of turns.
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        # Let the user guess a number.
        guess = int(input("Make a guess: "))

        # Check the user's guess and update the number of turns.
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")

