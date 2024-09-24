def easypeasy(s: str) -> str:
    '''
    This function takes a string `s` and removes consecutive duplicate characters.
    
    Parameters:
    s (str): The input string from which consecutive duplicates are to be removed.
    
    Returns:
    str: A new string with consecutive duplicates removed.
    '''
    if not s:
        return ''  # Return an empty string if the input is empty
    
    lastsym = s[0]  # Initialize the last seen symbol with the first character of the string
    ans = []  # Initialize an empty list to store the result characters
    
    for i in range(len(s)):
        if s[i] != lastsym:  # If the current character is different from the last seen character
            ans.append(lastsym)  # Append the last seen character to the result list
            lastsym = s[i]  # Update the last seen character to the current character
    
    ans.append(lastsym)  # Append the last seen character after the loop ends
    return ''.join(ans)  # Join the list into a string and return it

# Driver code to test the function
if __name__ == "__main__":
    # Example usage
    test_string = 'aaabbcddd'
    result = easypeasy(test_string)
    print(f"Input: '{test_string}' -> Output: '{result}'")  # Output: 'abcd'
    
    # Additional test cases
    print(easypeasy(''))  # Output: ''
    print(easypeasy('a'))  # Output: 'a'
    print(easypeasy('aa'))  # Output: 'a'
    print(easypeasy('aabbcc'))  # Output: 'abc'
    print(easypeasy('abc'))  # Output: 'abc'
    print(easypeasy('aabbccddeeff'))  # Output: 'abcdef'
