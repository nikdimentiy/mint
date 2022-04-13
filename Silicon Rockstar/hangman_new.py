import random
logo = """


 __    __   ______   __    __   ______   __       __   ______   __    __ 
/  |  /  | /      \ /  \  /  | /      \ /  \     /  | /      \ /  \  /  |
$$ |  $$ |/$$$$$$  |$$  \ $$ |/$$$$$$  |$$  \   /$$ |/$$$$$$  |$$  \ $$ |
$$ |__$$ |$$ |__$$ |$$$  \$$ |$$ | _$$/ $$$  \ /$$$ |$$ |__$$ |$$$  \$$ |
$$    $$ |$$    $$ |$$$$  $$ |$$ |/    |$$$$  /$$$$ |$$    $$ |$$$$  $$ |
$$$$$$$$ |$$$$$$$$ |$$ $$ $$ |$$ |$$$$ |$$ $$ $$/$$ |$$$$$$$$ |$$ $$ $$ |
$$ |  $$ |$$ |  $$ |$$ |$$$$ |$$ \__$$ |$$ |$$$/ $$ |$$ |  $$ |$$ |$$$$ |
$$ |  $$ |$$ |  $$ |$$ | $$$ |$$    $$/ $$ | $/  $$ |$$ |  $$ |$$ | $$$ |
$$/   $$/ $$/   $$/ $$/   $$/  $$$$$$/  $$/      $$/ $$/   $$/ $$/   $$/ 
                                                                         
                                                                         
                                                                         

"""

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["mantra", "speed", "gold", "hedonist", "rectangle",
             "rose", "envelope", "nirvana", "television", "movie"]


print(logo)
game_is_finished = False
lives = len(stages) - 1

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = []
for _ in range(word_length):
    display += "_"

while not game_is_finished:
    guess = input("🔥🔥🔥 Guess a letter: 😉🌏⭐---> : ").lower()
    print()

    if guess in display:
        print(f"🍀🍀🍀 You've already guessed {guess} 🍀🍀🍀")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        print()
        print(
            f"💢💢💢 You guessed {guess}, that's not in the word. You lose a life. 😩 💢💢💢")
        lives -= 1
        if lives == 0:
            game_is_finished = True
            print("You lose.")
            print(f"The guessed word is: ---> ⛔ {chosen_word.upper()} ⛔ <---")

    if not "_" in display:
        game_is_finished = True
        print("You win.")

    print(stages[lives])
