#  classic algorithm of binary search
def binary_search(user_list, item):
    low = 0
    high = len(user_list) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = user_list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1, 3, 5, 7, 9, 56, 76, 32, 90, 89, 34, 21, 67, 82, 100, 4, 8]
my_list.sort()

print(binary_search(my_list, 7))
print(binary_search(my_list, -1))
