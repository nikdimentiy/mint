def binarySearch(list: object, value: int) -> int:
    lower = 0
    high = len(list) - 1

    while lower <= high:
        middle = (lower + high) // 2
        guess = list[middle]
        if guess == value:
            return middle
        if guess > value:
            high = middle - 1
        else:
            lower = middle + 1
    return None


my_list = [1, 3, 5, 7, 6]
print(binarySearch(my_list, 7))
