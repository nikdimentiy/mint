def grabscrab(word, possible_words):
    words = []
    letters1 = {l: word.count(l) for l in word}
    for word in possible_words:
        letters2 = {l: word.count(l) for l in word}
        if letters1 == letters2:
            words.append(word)
    return words
