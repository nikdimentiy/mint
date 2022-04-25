word = input("Enter any word, please: ")
vowels = {'a', 'i', 'o', 'u', 'e'}
vowels_result = vowels.intersection(set(word))
result = " , ".join(vowels_result)

print(f"Vowels in entered word: {result}")
