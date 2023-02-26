# In this Kata, you will be given a string that may have mixed uppercase and lowercase letters
# and your task is to convert that string to either lowercase only or uppercase only based on: make as few changes as possible.
# if the string contains equal number of uppercase and lowercase letters, convert the string to lowercase.
# For example:

# solve("coDe") = "code". Lowercase characters > uppercase. Change only the "D" to lowercase.
# solve("CODe") = "CODE". Uppercase characters > lowecase. Change only the "e" to uppercase.
# solve("coDE") = "code". Upper == lowercase. Change all to lowercase.

def solve(s):
    uppercase_count = sum(1 for c in s if c.isupper())
    lowercase_count = sum(1 for c in s if c.islower())

    if uppercase_count > lowercase_count:
        return s.upper()
    elif lowercase_count > uppercase_count or uppercase_count == lowercase_count:
        return s.lower()
