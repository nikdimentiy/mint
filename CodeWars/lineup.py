def solution(commands):
    """
    Counts the number of commands after which all students (including those who mix up left and right) 
    end up facing the same direction.

    The commands are:
    - 'L': Turn left
    - 'R': Turn right
    - 'A': Turn around (180 degrees)

    Rules:
    - Some students interpret 'L' as 'R' and vice versa, while others follow commands correctly.
    - After certain commands, all students will face the same direction regardless of how they interpret 'L' and 'R'.

    Parameters:
    commands (str): A string consisting of commands ('L', 'R', 'A').

    Returns:
    int: The number of commands after which all students face the same direction.
    """
    # Variable to track the "weirdness" state (if students might differ in direction)
    weird = False
    # Counter for commands after which all students face the same direction
    total = 0

    # Process each command in the string
    for command in commands:
        if command == 'L' or command == 'R':
            # Toggle the weird state for 'L' and 'R' commands
            weird = not weird
        # If not weird (students face the same direction), increment total
        if not weird:
            total += 1

    return total

# Driver code to test the function
if __name__ == "__main__":
    # Define test cases
    commands_list = [
        "LLARL",  # Expected output: 3
        "LRLR",   # Expected output: 2
        "A",      # Expected output: 1
        "LLLL",   # Expected output: 2
        "RRRR",   # Expected output: 2
    ]

    # Test and print results for each case
    for commands in commands_list:
        result = solution(commands)
        print(f"Commands: {commands} -> Same Direction Count: {result}")
