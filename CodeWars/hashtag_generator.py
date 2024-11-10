def generate_hashtag(s):
    """
    Generate a hashtag from a given string.

    The hashtag will start with a '#' and will capitalize the first letter of each word.
    If the input string is empty or the resulting hashtag exceeds 140 characters, 
    the function will return False.

    Parameters:
    s (str): The input string from which to generate the hashtag.

    Returns:
    str or bool: The generated hashtag if valid, otherwise False.
    """
    # Check if the input string is empty or contains only whitespace
    if not s or len(s.strip()) == 0:
        return False
    
    # Create the hashtag by capitalizing the first letter of each word
    hashtag = "#" + "".join([w.strip().title() for w in s.split()])
    
    # Check if the length of the hashtag exceeds 140 characters
    if len(hashtag) > 140:
        return False
    
    return hashtag

# Driver code to test the function
if __name__ == "__main__":
    test_strings = [
        "hello world",          # Valid input
        "  python programming  ", # Valid input with extra spaces
        "",                     # Empty string
        "a" * 141,             # Exceeds 140 characters
        "This is a test of the hashtag generator", # Valid input
        "   ",                  # Only spaces
        "SingleWord"           # Valid single word
    ]

    for test in test_strings:
        result = generate_hashtag(test)
        print(f"Input: '{test}' => Output: {result}")
