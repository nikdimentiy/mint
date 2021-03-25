# the tiny code represent: many features of dictionary
favorite_lang = {
    'jen': 'ruby',
    'sarah': 'kotlin',
    'derek': 'python',
    'edward': 'java',
    'phil': 'lua',
    'anthony': 'scala',
    'brandon': 'python',
    'daniel': 'csharp',
    'kevin': 'java',
    'eric': 'javascript',
    'frank': 'julia',
    'harry': 'swift',
    'jonathan': 'java',
    'mike': 'rust',
    'noah': 'python',
    'patrick': 'javascript',
}

friends = ['phil', 'sarah', 'derek']
for name in favorite_lang.keys():
    if name in friends:
        print("Hi " + name.title() + ", I see you favorite language is " + favorite_lang[name].title() + "!")

print()

print("The following languages have been mentioned: ")
for language in sorted(favorite_lang.values()):
    print(language.title())

print()
print("The unique list of programming languages: ")
for language in set(favorite_lang.values()):
    print(language.title())

# list of dictionary

alien_0 = {'color': 'green', 'points': 5} # dictionary 1
alien_1 = {'color': 'yellow', 'points': 10} # dictionary 2
alien_2 = {'color': 'red', 'points': 15} # dictionary 3

aliens = [alien_0, alien_1, alien_2] # the total list of dictionaries

for alien in aliens:
    print(alien)

# creating a new empty list for storage of aliens
aliens = []
# creating 30 new green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# output of first new aliens 
for alien in aliens[:5]:
    print(alien)
print("...")

# the output of total quantity of aliens
print("Total number of aliens: " + str(len(aliens)))



