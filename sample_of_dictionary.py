# the tiny code represent: many features of dictionary
favorite_lang = {
    'jen': 'ruby',
    'sarah': 'kotlin',
    'derek': 'python',
    'edward': 'java',
    'phil': 'lua'
}

friends = ['phil', 'sarah', 'derek']
for name in favorite_lang.keys():
    if name in friends:
        print("Hi " + name.title() + ", I see you favorite language is " + favorite_lang[name].title() + "!")

print()

print("The following languages have been mentioned: ")
for language in sorted(favorite_lang.values()):
    print(language.title())
