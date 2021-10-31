# hangman game
import random
# creating list of guess words
word_list = ["ardvark", "baboon", "camel",
             "macaque", "gibbon", "lion",
             "elephant", "leopard", "rhinocerous",
             "bufafalo", "cheetah", "giraffe"]

chosen_word = random.choice(word_list)  # random choice of guess word
word_length = len(chosen_word)  # calculate length of the guess word
print(f"The solution is {chosen_word}.")  # intermediate check

# create blanks
display = []
for _ in range(word_length):
    display += "_"
print(display)

end_of_game = False

while not end_of_game:
    guess = input("Guess a leter: ").lower()

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        print(
            f"Current position: {position}\n Current leter: {letter}\n Guessed letter: {guess}")

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win!")
