# Your task is to remove all consecutive duplicate words from a string, leaving only first words entries. For example:

# "alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"

# --> "alpha beta gamma delta alpha beta gamma delta"


from itertools import groupby


def remove_consecutive_duplicates(s):
    return ' '.join(k for k, _ in groupby(s.split()))
