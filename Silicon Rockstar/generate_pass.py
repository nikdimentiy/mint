"""
Generate a random password.

Args:
  length (int, optional): The length of the password. Defaults to 8.

Returns:
  str: A random password.

Example:

>>> password = generate_password()
>>> print("Generated password:", password)
Generated password: !h4#345678
"""

import random
import string


def generate_password(length=8):
  """Generate a random password.

  Args:
    length (int, optional): The length of the password. Defaults to 8.

  Returns:
    str: A random password.
  """

  characters = string.ascii_letters + string.digits + string.punctuation
  password = ''.join(random.choice(characters) for _ in range(length))
  return password


# Example usage:

password = generate_password()
print("Generated password:", password)
