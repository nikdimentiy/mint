
# The assignment as it was completed during the workshop is commented out at the bottom.

# Assignment with the characters set up as dictionaries (composite data types) and all bonus tasks added:

while True:  # while loop enclosing the entire game for exiting/playing again purposes
    wizard = {"name": "Wizard", "hp": 70, "damage": 150}
    elf = {"name": "Elf", "hp": 100, "damage": 100}
    human = {"name": "Human", "hp": 150, "damage": 20}
    ent = {"name": "Ent", "hp": 125, "damage": 111}
    dragon = {"name": "Dragon", "hp": 300, "damage": 50}

    # Character selection with characters set up as dictionaries:
    while True:
        print("\nCharacter Options:")
        print("1.   Wizard")
        print("2.   Elf")
        print("3.   Human")
        print("4.   Ent")  # fourth option (tree creatures from Lord of the Rings)
        character_choice = input("Choose your character or press x to exit the game: ")  # option to exit
        if character_choice == "1" or character_choice.lower() == "wizard":  # bonus tasks 1 and 2
            character = wizard
            my_hp = wizard["hp"]
            my_damage = wizard["damage"]
            break
        if character_choice == "2" or character_choice.lower() == "elf":  # bonus tasks 1 and 2
            character = elf
            my_hp = elf["hp"]
            my_damage = elf["damage"]
            break
        if character_choice == "3" or character_choice.lower() == "human":  # bonus tasks 1 and 2
            character = human
            my_hp = human["hp"]
            my_damage = human["damage"]
            break
        if character_choice == "4" or character_choice.lower() == "ent":  # bonus tasks 1 and 2
            character = ent
            my_hp = ent["hp"]
            my_damage = ent["damage"]
            break
        if character_choice.lower() == "x":  # if user wants to exit...
            break  # break out of the character assignment loop
        print("\nUnknown Character")
        
    if character_choice.lower() == "x":  # check again if input indicated a desire to exit the game
        print("\nGoodbye!\n")
        break  # break out of the while loop that encloses the entire game to exit
        
    print("\nYou have chosen the character:", character["name"])
    print("Health:", my_hp)
    print("Damage:", my_damage)  

    # Battle time with characters set up as dictionaries:
    while True:
        dragon["hp"] = dragon["hp"] - my_damage
        print("\nThe", character["name"], "damaged the Dragon!")
        print("The Dragon's hitpoints are now:", dragon["hp"])
        if dragon["hp"] <= 0:
            print("\nThe Dragon has lost the battle.")
            break
        my_hp = my_hp - dragon["damage"]
        print("\nThe Dragon strikes back at", character["name"]  + "!")
        print("The", character["name"] + "'s hitpoints are now:", my_hp)
        if my_hp <= 0:
            print("\nThe", character["name"], "has lost the battle.")
            break
                 
    # Check if user wants to play again:            
    playAgain = input("\nWould you like to play again? ")  
    if playAgain.lower() == "y" or playAgain.lower() == "yes":
        continue  # start another iteration of the game-enclosing while loop
    elif playAgain.lower() == "n" or playAgain.lower() == "no":
        print("\nGoodbye!\n")
        break  # break out of the game-enclosing while loop
    else:
        print("\nThat wasn't an intelligible answer. \nPlease restart the game if you " + 
            "decide you want to play again.\n")
        break  # break out of the game-enclosing while loop




# For some reason when you mentioned setting up each character as a composite
# data type, I thought of doing it as just general objects as opposed to say, 
# dictionaries, so I decided to try it that way as well...

# Assignment with the characters set up as Character objects (with all bonus tasks added):
"""
while True:  # while loop enclosing the entire game for exiting/playing again purposes
    class Character:
        def __init__(self, name, hp, damage):
            self.name = name
            self.hp = hp
            self.damage = damage

    wizard = Character("Wizard", 70, 150) 
    elf = Character("Elf", 100, 100) 
    human = Character("Human", 150, 20) 
    ent = Character("Ent", 125, 111) 
    dragon = Character("Dragon", 300, 50)

    # Character selection with Character objects:
    while True:
        print("\nCharacter Options:")
        print("1.   Wizard")
        print("2.   Elf")
        print("3.   Human")
        print("4.   Ent")  # fourth option (tree creatures from Lord of the Rings)
        character_choice = input("Choose your character or press x to exit the game: ")  # option to exit
        if character_choice == "1" or character_choice.lower() == "wizard":  # bonus tasks 1 and 2
            character = wizard
            my_hp = wizard["hp"]
            my_damage = wizard["damage"]
            break
        if character_choice == "2" or character_choice.lower() == "elf":  # bonus tasks 1 and 2
            character = elf
            my_hp = elf.hp
            my_damage = elf.damage
            break
        if character_choice == "3" or character_choice.lower() == "human":  # bonus tasks 1 and 2
            character = human
            my_hp = human.hp
            my_damage = human.damage
            break
        if character_choice == "4" or character_choice.lower() == "ent":  # bonus tasks 1 and 2
            character = ent
            my_hp = ent.hp
            my_damage = ent.damage
            break
        if character_choice.lower() == "x":  # if user wants to exit...
            break  # break out of the character assignment loop
        print("Unknown Character")
        
    if character_choice.lower() == "x":  # check again if input indicated a desire to exit the game
        print("\nGoodbye!\n")
        break  # break out of the while loop that encloses the entire game to exit
            
    print("You have chosen the character:", character.name)
    print("Health:", my_hp)
    print("Damage:", my_damage)  
        
    # Battle time with Character objects:     
    while True:
        dragon.hp = dragon.hp - my_damage
        print("\nThe", character.name, "damaged the Dragon!")
        print("The Dragon's hitpoints are now:", dragon.hp)
        if dragon.hp <= 0:
            print("\nThe Dragon has lost the battle.")
            break
        my_hp = my_hp - dragon.damage
        print("\nThe Dragon strikes back at", character.name  + "!")
        print("The", character.name + "'s hitpoints are now:", my_hp)
        if my_hp <= 0:
            print("\nThe", character.name, "has lost the battle.")
            break
            
    # Check if user wants to play again:            
    playAgain = input("\nWould you like to play again? ")  
    if playAgain.lower() == "y" or playAgain.lower() == "yes":
        continue  # start another iteration of the game-enclosing while loop
    elif playAgain.lower() == "n" or playAgain.lower() == "no":
        print("\nGoodbye!\n")
        break  # break out of the game-enclosing while loop
    else:
        print("\nThat wasn't an intelligible answer. \nPlease restart the game if you " + 
            "decide you want to play again.\n")
        break  # break out of the game-enclosing while loop
"""




# Assignment with the original variable setup as per the instructions (with bonus tasks 1, 2, and 3):
"""
wizard_hp = 70
elf_hp = 100
human_hp = 150
ent_hp = 125

wizard_damage = 150
elf_damage = 100
human_damage = 20
ent_damage = 111

dragon_hp = 300
dragon_damage = 50

# Character selection with the original variable setup:
while True:
    print("\nCharacter Options:")
    print("1.   Wizard")
    print("2.   Elf")
    print("3.   Human")
    print("4.   Ent")
    character_choice = input("Choose your character: ")
    if character_choice == "1" or character_choice.lower() == "wizard":
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    if character_choice == "2" or character_choice.lower() == "elf":
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break
    if character_choice == "3" or character_choice.lower() == "human":
        character = human
        my_hp = human_hp
        my_damage = human_damage
        break
    if character_choice == "4" or character_choice.lower() == "ent":
        character = ent
        my_hp = ent_hp
        my_damage = ent_damage
        break
    print("Unknown Character")
    
print("You have chosen the character:", character)
print("Health:", my_hp)
print("Damage:", my_damage)                

# Battle time with the original variable setup:       
while True:
    dragon_hp = dragon_hp - my_damage
    print("The", character, "damaged the Dragon!")
    print("The Dragon's hitpoints are now:", dragon_hp)
    if dragon_hp <= 0:
        print("The Dragon has lost the battle.")
        break
    my_hp = my_hp - dragon_damage
    print("The Dragon strikes back at", character  + "!")
    print("The", character + "'s hitpoints are now:", my_hp)
    if my_hp <= 0:
        print("The", character, "has lost the battle.")
        break
"""