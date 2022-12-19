# An isogram is a word that has no repeating letters, consecutive or non-consecutive.
# Implement a function that determines whether a string that contains only letters is an isogram.
# Assume the empty string is an isogram. Ignore letter case.

# Example

# is_isogram("Dermatoglyphics" ) == true
# is_isogram("aba" ) == false
# is_isogram("moOse" ) == false # -- ignore letter case

def is_isogram(string):
    string = string.lower()
    letters = {letter: string.count(letter) for letter in string}
    if set(letters.values()) == {1} or set(letters.values()) == set():
        return True
    else:
        return False
