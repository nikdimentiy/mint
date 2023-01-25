def funny_Cesar_cipher(message):
    abc = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLM'
    r = ""
    for char in message:
        if char in abc:
            r += abc[abc.index(char) + 13]
        else:
            r += char
    return r


result = funny_Cesar_cipher("hello man!")
print(result)