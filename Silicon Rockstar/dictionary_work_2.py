favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}


for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

for name in favorite_languages.keys():
    print(name.title())

for name in favorite_languages.values():
    print(name.title())


friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print(" Hi " + name.title() + ", I see your favorite language is " +
              favorite_languages[name].title() + "!")


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")


for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")


print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
