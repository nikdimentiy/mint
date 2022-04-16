# search: the shortest words in the sequence and display
# them separated by a space

def shortwords(words):
    minlen = len(words[0])
    for word in words:
        if len(word) < minlen:
            minlen = len(words)
    ans = []
    for word in words:
        if len(word) == minlen:
            ans.append(word)
    return ' '.join(ans)
