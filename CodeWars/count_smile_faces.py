def count_smileys(arr):
    """
    Count the number of smiley faces in a list of strings.

    A smiley face is defined as:
    - A string of length 2: either ":)" or ":D" or ";)" or ";D"
    - A string of length 3: either ":~)" or ":~D" or ";~)" or ";~D" or ": -)" or ": -D" or "; -)" or "; -D"

    Parameters:
    arr (list of str): A list of strings to check for smiley faces.

    Returns:
    int: The count of smiley faces in the input list.
    """
    smileys = []  # List to store valid smiley faces
    for s in arr:
        # Check for 2-character smileys
        if len(s) == 2 and s[0] in [":", ";"] and s[-1] in [")", "D"]:
            smileys.append(s)
        # Check for 3-character smileys
        elif len(s) == 3 and s[0] in [":", ";"] and s[1] in ["-", "~"] and s[-1] in [")", "D"]:
            smileys.append(s)
    
    return len(smileys)  # Return the count of smileys

# Driver code to test the function
if __name__ == "__main__":
    test_arr = [":)", ";D", ":~)", ":~D", ";-)", ";-D", ":-)", ":-D", ":-", ":-D", "hello", ":)"]
    smiley_count = count_smileys(test_arr)
    print(f"Number of smileys in the list: {smiley_count}")  # Expected output: 8
