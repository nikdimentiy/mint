import re  # Import the regular expression module to perform pattern matching.

# Prompt the user to input a URL and remove leading/trailing whitespaces.
url = input("URL: ").strip()

# Use a regular expression to search for a specific pattern in the input URL:
# - Starts with "http://" or "https://"
# - Followed by an optional "www."
# - Followed by "twitter.com/"
# - Captures the username (a sequence of lowercase letters, digits, and underscores)
# - Performs a case-insensitive search
matches = re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE)

if matches:
    # If a match is found, print the captured username (group 1).
    print("Username:", matches.group(1))
