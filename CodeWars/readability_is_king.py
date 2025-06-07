import re

def flesch_kincaid(text: str) -> float:
    """
    Calculate the Flesch-Kincaid grade level for a given string of text.

    The Flesch-Kincaid grade level is an approximation of the U.S. school grade level 
    that can understand the text. A higher grade level indicates that the text is 
    more complex and may be difficult for younger readers.

    The formula used is:
        Grade Level = 0.39 * (Total Words / Total Sentences) + 
                      11.8 * (Total Syllables / Total Words) - 15.59

    Args:
        text (str): The text to analyze.

    Returns:
        float: The Flesch-Kincaid grade level rounded to two decimal points.
    """
    
    def _words(s):
        """Extract words from a sentence, removing non-alphabetic characters."""
        return [''.join(c for c in w if c.isalpha()) for w in s.split()]

    def _syllables(ws):
        """Count the total number of syllables in a list of words."""
        return sum(max(len(re.findall('[aeiou]+', w)), 1) for w in ws)

    # Split the text into sentences based on punctuation marks
    sentences = [_words(s) for s in re.split(r'[.!?]+', text.lower()) if s]
    
    # Calculate the total number of words
    total_words = sum(len(w) for w in sentences)
    
    # Calculate the total number of syllables
    total_syllables = sum(_syllables(s) for s in sentences)
    
    # Calculate the number of sentences
    total_sentences = len(sentences)

    # Calculate the Flesch-Kincaid grade level
    if total_sentences == 0 or total_words == 0:
        return 0.0  # Avoid division by zero

    p1 = 0.39 * (total_words / total_sentences)
    p2 = 11.8 * (total_syllables / total_words)
    
    return round(p1 + p2 - 15.59, 2)

# Driver code to test the function
if __name__ == "__main__":
    sample_text = (
        "The Flesch-Kincaid readability tests are designed to indicate how difficult 
        a passage in English is to understand. The tests use the average number of 
        syllables per word and the average number of words per sentence to calculate 
        a score."
    )
    
    grade_level = flesch_kincaid(sample_text)
    print(f"The Flesch-Kincaid grade level of the sample text is: {grade_level}")
