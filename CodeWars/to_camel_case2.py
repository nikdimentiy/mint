def to_camel_case(text):
    """
    Converts dash/underscore delimited words into camel casing.
    
    The first word within the output is capitalized only if the original
    word was capitalized (Upper Camel Case/Pascal case).
    
    Args:
        text (str): The dash/underscore delimited string to convert
        
    Returns:
        str: The camel cased string
        
    Examples:
        >>> to_camel_case("the-stealth-warrior")
        "theStealthWarrior"
        >>> to_camel_case("The_Stealth_Warrior")
        "TheStealthWarrior"
    """
    # Return empty string if input is empty
    if not text:
        return ""
    
    # Split the text by dash or underscore
    words = text.replace('-', '_').split('_')
    
    # Keep the first word as is (maintaining original capitalization)
    result = words[0]
    
    # Capitalize the first letter of each remaining word and add to result
    for word in words[1:]:
        result += word.capitalize()
    
    return result


# Driver code
if __name__ == "__main__":
    test_cases = [
        "the-stealth-warrior",
        "The-Stealth-Warrior",
        "the_stealth_warrior",
        "The_Stealth_Warrior",
        "TheStealthWarrior",
        "",
        "a-b-c",
        "A-b-c"
    ]
    
    for test in test_cases:
        print(f'"{test}" -> "{to_camel_case(test)}"')
