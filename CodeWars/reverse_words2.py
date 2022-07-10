def reverse_words(str):
    # go for it
    newStr = []
    for i in str.split(' '):
        newStr.append(i[::-1])
    return ' '.join(newStr)


text = "This is an example!"  # ==> "sihT si na !elpmaxe"
print(reverse_words(text))
