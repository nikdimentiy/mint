# Python code to check for empty list
# Explicit way
def is_empty(list_1):
    if len(list_1) == 0:
        return 0
    else:
        return 1


# Driver Code
# list_1 = []
list_1 = [4, 7, 9, 23, 4, 7, 9, 0, 1, 2]
result = is_empty(list_1)

if result:
    print("The list is not empty")
else:
    print("Empty List")





