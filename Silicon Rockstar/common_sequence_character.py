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
