def dashatize(n):
    """
    Convert an integer into a string with dashes around odd digits.

    This function takes an integer and returns a string representation of that integer,
    where each odd digit is surrounded by dashes. If the input is not an integer,
    the function returns "None".

    Args:
        n (int): The integer to be converted.

    Returns:
        str: A string representation of the integer with dashes around odd digits,
             or "None" if the input is not an integer.
    """
    # Print the input value for debugging purposes
    print(n)
    
    # Check if the input is an integer
    if type(n) == int:
        # Convert the absolute value of the integer to a string
        n = str(abs(n))
        new = ""
        
        # Iterate through each digit in the string representation
        for e, i in enumerate(n):
            # Check if the digit is odd
            if int(i) % 2 != 0:
                # Add dashes around odd digits based on their position
                if e == 0:
                    new += "{}-".format(i)  # Add dash after the first odd digit
                elif e == len(n) - 1:
                    new += "-{}".format(i)  # Add dash before the last odd digit
                else:
                    new += "-{}-".format(i)  # Add dashes around middle odd digits
            else:
                new += i  # Add even digits without modification
        
        # Remove trailing dash if present
        if new[-1] == "-":
            new = new[:-1]
        
        # Replace any double dashes with a single dash
        return new.replace("--", "-")
    else:
        return "None"  # Return "None" if the input is not an integer

# Driver code to test the dashatize function
if __name__ == "__main__":
    # Test cases
    test_cases = [123, -456, 0, 13579, 24680, "string", None, 101]

    # Iterate through test cases and print the results
    for i, test in enumerate(test_cases):
        print(f"Test case {i + 1}: {test} => Result: {dashatize(test)}")
