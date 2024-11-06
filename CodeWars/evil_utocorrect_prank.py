import re

def autocorrect(input):
    """
    This function takes a string as input and replaces all occurrences of the word 'u' or 'you' 
    (case insensitive) with the phrase 'your sister'. 

    Parameters:
    input (str): The input string that may contain the words 'u' or 'you'.

    Returns:
    str: The modified string with 'u' or 'you' replaced by 'your sister'.
    """
    # Use a regular expression to find and replace 'u' or 'you' with 'your sister'
    return re.sub(r'(?i)\b(u|you+)\b', "your sister", input)

# Driver code to test the autocorrect function
if __name__ == "__main__":
    test_strings = [
        "u are awesome!",
        "You should try this.",
        "I can't believe u did that!",
        "Youuu are the best!",
        "This is a test without the words.",
        "U and you are both here."
    ]

    for test in test_strings:
        corrected = autocorrect(test)
        print(f"Original: {test}\nCorrected: {corrected}\n")
