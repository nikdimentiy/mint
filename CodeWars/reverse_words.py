def reverse_words(text):
    return " ".join([word[::-1] for word in text.split(" ")])


text = "This is an example!"  # ==> "sihT si na !elpmaxe"
print(reverse_words(text))
