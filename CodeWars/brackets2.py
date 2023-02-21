# Write a function that takes a string of parentheses, and determines if the order of the parentheses
# is valid. The function should return true if the string is valid, and false if it's invalid.

# Examples
# "()"              =>  true
# ")(()))"          =>  false
# "("               =>  false
# "(())((()())())"  =>  true


def valid_parentheses(string):
    string = "".join(ch for ch in string if ch in "()")
    while "()" in string:
        string = string.replace("()", "")
    return not string
