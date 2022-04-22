my_string = input()
answer = ""
answer_count = 0
for i in range(len(my_string)):
    now_count = 0
    for j in range(len(my_string)):
        if my_string[i] == my_string[j]:
            now_count += 1
        if now_count > answer_count:
            answer = my_string[i]
            answer_count = now_count
print(answer)  # Big O notation = O(n^2)

######################################################################################
my_string = input()
answer = ""
answer_count = 0
for letter in set(my_string):
    now_count = 0
    for j in range(len(my_string)):
        if letter == my_string[j]:
            now_count += 1
        if now_count > answer_count:
            answer = letter
            answer_count = now_count
print(answer)  # Big O notation = O(n K), where "K" is the number of different symbols

#####################################################################################

# user input, define variables and constant
my_string = input("Enter the some string sequence: ")
answer = ""
answer_count = 0
my_dictionary = {}

# computation logic (algorithm)
for now in my_string:
    if now not in my_dictionary:
        my_dictionary[now] = 0
    my_dictionary[now] += 1
for key in my_dictionary:
    if my_dictionary[key] > answer_count:
        answer_count = my_dictionary[key]
        answer = key

# output result
print(f"The most common sequence character is: {answer}")  # Big O notation = O(n)
print(f"The number of occurrences of this symbol in the sequence is: : {answer_count}")
