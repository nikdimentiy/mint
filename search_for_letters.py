def search4vowels(phrase: str) -> set:
    """Returns the set of vowels found in 'phrase'."""

    return set('aeiou').intersection(set(phrase))


phrase = input("Enter anything phrase, please: ")
print("Vowels in this phrase is: : ", search4vowels(phrase))


def search4letters(phrase: str, letters: str = 'aeiou') -> set:
    """Returns the set of 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))


phrase = input("Enter phrase, please: ")
letters = input("Enter anything letters, for find in entered phrase: ")
print("Needed letters in this phrase is: : ", search4letters(phrase, letters))
