# Write a function named first_non_repeating_letter that takes a string input, 
# and returns the first character that is not repeated anywhere in the string.


def first_non_repeating_letter(string):
    singles = [i for i in string if string.lower().count(i.lower()) == 1]
    return singles[0] if singles else ''
