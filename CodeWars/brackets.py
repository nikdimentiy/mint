# Write a function that takes a string of parentheses, and determines if the order of the parentheses
# is valid. The function should return true if the string is valid, and false if it's invalid.

# Examples
# "()"              =>  true
# ")(()))"          =>  false
# "("               =>  false
# "(())((()())())"  =>  true


def valid_parentheses(string):
    # Initialize a counter for the balance of parentheses
    balance = 0
    # Loop through each character in the string
    for char in string:
        # If the character is an opening parenthesis, increase the balance by 1
        if char == "(":
            balance += 1
        # If the character is a closing parenthesis, decrease the balance by 1
        elif char == ")":
            balance -= 1
        # If the balance becomes negative at any point, return false
        if balance < 0:
            return False
    # If the balance is zero at the end, return true
    return balance == 0
