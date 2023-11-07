import re  # Import the regular expression module to perform pattern matching.

# Prompt the user to input their email and remove leading/trailing whitespaces.
email = input("What's your email? ").strip()

# Use regular expressions to check if the email follows a specific pattern:
# - Starts with one or more word characters (letters, digits, or underscores)
# - Followed by an "@" symbol
# - Followed by an optional subdomain (zero or one occurrence of word characters and a dot)
# - Followed by one or more word characters
# - Ends with ".com" in a case-insensitive manner
if re.search(r"^\w+@(\w+\.)?\w+\.com$", email, re.IGNORECASE):
    print("Valid")  # If the email matches the pattern, print "Valid."
else:
    print("Invalid")  # If the email does not match the pattern, print "Invalid."
