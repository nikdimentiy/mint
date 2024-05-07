def validate_line(line):
    """
    Validate a given string based on specific rules:
    1. If it contains underscores ('_'), they are removed.
    2. If it doesn't contain a hash symbol ('#'), it should be convertible to an integer.
    3. If it contains a hash symbol, the part before the first hash should be a base (from 2 to 16),
       and the part between the hashes should be convertible to an integer with that base.

    :param line: A string to validate.
    :return: True if the string meets the specified conditions, otherwise False.
    """
    # Remove underscores from the line
    line = line.replace("_", "")

    # If there's no hash symbol, attempt to convert the line to an integer
    if "#" not in line:
        try:
            # Try to convert the entire line to an integer
            int(line)
        except ValueError:
            # If conversion fails, return False
            return False
    else:
        # If there's a hash symbol, determine the base and the value
        try:
            # Extract the base from the part before the first hash
            base_pos = line.find("#")
            base = int(line[:base_pos])

            # Ensure the base is between 2 and 16
            if base < 2 or base > 16:
                return False

            # Extract the value between the two hash symbols and convert it using the base
            value_str = line[base_pos + 1:line.rfind("#")]
            n = int(value_str, base)
        except ValueError:
            # If base or value conversion fails, return False
            return False

    # If everything is successful, return True
    return True


# Driver code to test the function with various cases
if __name__ == "__main__":
    # Test cases
    test_lines = [
        "1234",       # Valid integer
        "1_234",      # Valid with underscores removed
        "2#10#1",     # Valid with base 2
        "16#f#",      # Valid with base 16
        "10#123#",    # Valid with base 10
        "2#101#",     # Valid with binary number
        "1#10#",      # Invalid: base less than 2
        "17#10#",     # Invalid: base greater than 16
        "abc",        # Invalid: not a number
        "2#xyz#",     # Invalid: non-numeric value for base 2
    ]

    # Validate and print results
    for line in test_lines:
        is_valid = validate_line(line)
        print(f"'{line}': {is_valid}")
