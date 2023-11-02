def search4vowels(phrase: str) -> set:
    """
    Returns the set of vowels found in the input 'phrase'.

    Args:
        phrase (str): The input string in which to search for vowels.

    Returns:
        set: A set containing the vowels found in the 'phrase'.
    """
    # Create a set containing the vowels 'a', 'e', 'i', 'o', and 'u'.
    vowels = set('aeiou')
    
    # Use the 'intersection' method to find the common elements between the set of vowels and the characters in the 'phrase'.
    found_vowels = vowels.intersection(set(phrase))
    
    # Return the set of found vowels.
    return found_vowels

def search4letters(phrase: str, letters: str = 'aeiou') -> set:
    """
    Returns the set of specified 'letters' found in the input 'phrase'.

    Args:
        phrase (str): The input string in which to search for specified 'letters'.
        letters (str, optional): A string containing the letters to search for. Defaults to 'aeiou'.

    Returns:
        set: A set containing the specified 'letters' found in the 'phrase'.
    """
    # Create a set containing the specified 'letters' to search for, with a default value of 'aeiou'.
    letters_to_search = set(letters)
    
    # Use the 'intersection' method to find the common elements between the set of specified 'letters' and the characters in the 'phrase'.
    found_letters = letters_to_search.intersection(set(phrase))
    
    # Return the set of found specified 'letters'.
    return found_letters
