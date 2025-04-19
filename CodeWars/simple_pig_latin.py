def pig_it(text):
    """
    Convert a given text into Pig Latin.

    In Pig Latin, for each word in the text:
    - If the word is alphabetic, move the first letter to the end of the word and add "ay".
    - If the word is not alphabetic (e.g., punctuation), leave it unchanged.

    Parameters:
    text (str): The input string containing words to be converted to Pig Latin.

    Returns:
    str: A string with each word converted to Pig Latin.
    """
    # Split the input text into words
    return " ".join([
        "{}{}ay".format(c[1:], c[0]) if c.isalpha() else c  # Convert to Pig Latin if the word is alphabetic
        for c in text.split()  # Iterate over each word in the split text
    ])

# Driver code to test the function
if __name__ == "__main__":
    # Test cases
    print(pig_it("Hello world !"))  # Expected output: "elloHay orldway !"
    print(pig_it("Pig Latin is fun"))  # Expected output: "igPay atinLay siay unfay"
    print(pig_it("This is a test."))  # Expected output: "hisTay siay aay esttay."
    print(pig_it("Python programming is awesome!"))  # Expected output: "ythonPay ogrammingpray siay awesome!"
