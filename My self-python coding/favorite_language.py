# dictionary: tiny code with cycle "for"

favorite_lang = {
    'jen': 'python',
    'phill': 'ruby',
    'sarah': 'java',
    'edward': 'c',
    'donovan': 'scala',
    'hanna': 'swift',
}

for name, language in favorite_lang.items():
    print(name.title() + " favorite language is " + language.title() + "!")
