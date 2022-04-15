def check_type_of_elements_in_list(seq):
    return all(isinstance(seq[i], int) for i in range(len(seq)))


my_list = [1, 3, 5, "hello"]

answer = check_type_of_elements_in_list(my_list)

if answer:
    print("All elements of list --> are integers.")
else:
    print("Not all elements of list --> are integers.")

check_type_of_elements_in_list(my_list)
