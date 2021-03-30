# The code output the sum of the indexes (two neighbors for each element of a list)
# For elements at the end of the list  - is one of the neighbors is the element that is at the opposite end of this list

initial_list = [int(i) for i in input().split()]
sum_list = []
left_index = -1
right_index = -len(initial_list) + 1
middle_index = 0
if len(initial_list) == 1:
    print(" ".join([str(elem) for elem in initial_list]))
else:
    while middle_index < len(initial_list):
        sum_list.append(initial_list[left_index] + initial_list[right_index])
        left_index += 1
        right_index += 1
        middle_index += 1
    initial_list = ' '.join([str(elem) for elem in sum_list])

    print(initial_list)
