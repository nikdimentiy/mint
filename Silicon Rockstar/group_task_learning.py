list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# for i in range(len(list1)):
#     print(type(list1[i]))

output = [print(list1[i]) for i in range(len(list1)) if list1[i] % 2 == 0]


output = [str(x) for x in list1]
print(output)
print(type(output))

new_string = " ".join(output)
print(new_string)
print(type(new_string))

greeting = "Hello "
phrase = greeting + new_string
print(phrase)
