def decodeMorse(morse_sequence):
    words = []
    for morse_word in morse_sequence.split('   '):
        word = ''.join(MORSE_CODE.get(morse_char, '')
                       for morse_char in morse_word.split(' '))
        if word:
            words.append(word)
    return ' '.join(words)
