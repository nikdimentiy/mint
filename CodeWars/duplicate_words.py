# Your task is to remove all consecutive duplicate words from a string, leaving only first words entries. For example:

# "alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"

# --> "alpha beta gamma delta alpha beta gamma delta"


def remove_consecutive_duplicates(text):
    words = text.split()
    unique_words = [words[0]]
    for i in range(1, len(words)):
        if words[i] != words[i-1]:
            unique_words.append(words[i])
    return ' '.join(unique_words)
