def find_most_frequent_character(s):
    """
    This function takes a string as input, iterates through its unique characters, and finds the most frequent character.
    
    Parameters:
    s (str): The input string
    
    Returns:
    tuple: A tuple containing the most frequent character and its count
    """

    # Initialize variables
    ans = ""
    anscnt = 0

    # Iterate through unique characters in the input string
    for now in set(s):
        nowcnt = 0

        # Count occurrences of the current character in the entire string
        for j in range(len(s)):
            if now == s[j]:
                nowcnt += 1

        # Update the most frequent character if needed
        if nowcnt > anscnt:
            ans = now
            anscnt = nowcnt

    # Print the result
    print("The most frequent character is:", ans, "-> appearing", anscnt, "times.")

# Test the function
input_string = input("Enter a string: ")
find_most_frequent_character(input_string)
