def searchvowels(phrase: str) -> set:
    """The function returns vowels letters in entered string"""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))
