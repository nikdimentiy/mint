vowels = set("aeiou")
word = input("Provide a word to search for vowels: ")
found = vowels.intersection(set(word))


print("Vowels in the word entered: ")
for vowel in found:
    print(vowel)

