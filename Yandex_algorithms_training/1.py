def find_most_frequent_character(s):
    """
    This function takes a string as input, iterates through it, and finds the most frequent character.
    
    Parameters:
    s (str): The input string
    
    Returns:
    tuple: A tuple containing the most frequent character and its count
    """
    
    # Print the entered string
    print(s)

    # Initialize variables
    ans = ""
    anscnt = 0

    # Iterate through the string
    for i in range(len(s)):

        nowcnt = 0

        # Count occurrences of the current character
        for j in range(len(s)):
            if s[i] == s[j]:
                nowcnt += 1

        # Update the most frequent character if needed
        if nowcnt > anscnt:
            ans = s[i]
            anscnt = nowcnt

    # Print the result
    print(ans, anscnt)

# Test the function
input_string = input("Enter a string: ")
find_most_frequent_character(input_string)
