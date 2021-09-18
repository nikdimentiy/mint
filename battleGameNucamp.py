"""
    ---> THE FIRST PROGRAM-GAME IN NUCAMP BOOTCAMP <---
"""

# announce (declare) game characters for the game

wizard = "Wizard"
elf = "Elf"
human = "Human"

# set hitpoints for each game characters (which means remaining health)

wizard_hp = 70
elf_hp = 100
human_hp = 150

# set damage indicator for each game characters (how hard they hit)
wizard_damage = 150
elf_damage = 100
human_damage = 20

# declare the main opponent in the game, and set health point and damage indicator
dragon = "Dragon"
dragon_hp = 300
dragon_damage = 50

# promt the player to choose from a list options
# and assign the selection result to the appropriate variables
while True:
    print("1)   Wizard")
    print("2)   Elf")
    print("3)   Human")
    character = int(input("Choose your character: "))
    if character == 1:
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    elif character == 2:
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break
    elif character == 3:
        character = human
        my_hp = human_hp
        my_damage = human_damage
        break
    else:
        print("Unknown character")

print("You have chosen the character: ", character)
print("Health: ", my_hp)
print("Damage: ", my_damage)
