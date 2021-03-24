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

