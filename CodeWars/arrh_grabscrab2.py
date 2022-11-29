def grabscrab(word, possible_words):
    return [w for w in possible_words if sorted(word) == sorted(w)]
