vowels = ["a", "e", "i", "o", "u"]
word = input("Enter a word to search for vowels: ")
found = []

for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for vowel in found:
    print(vowel)


vowels = ["a", "e", "i", "o", "u"]
word = input("Enter a word to search for vowels: ")
found = {}

found["a"] = 0
found["e"] = 0
found["i"] = 0
found["o"] = 0
found["u"] = 0

for letter in word:
    if letter in vowels:
        found[letter] += 1

for key, value in sorted(found.items()):
    print(key, "was found", value, "time(s).")


vowels = ["a", "e", "i", "o", "u"]
word = input("Enter a word to search for vowels: ")
found = {}

for letter in word:
    if letter in vowels:
        found.setdefault(letter, 0)
        found[letter] += 1

for key, value in sorted(found.items()):
    print(key, "was found", value, "time(s).")
