def comp(*args):
    try:
        if len(args) < 2 or type(args[1]) == 'NoneType':
            return False
        array1 = args[0]
        print(type(args[1]))

        array2 = args[1]
        print(array1)
        print(args[1])
        array1 = [_ * _ for _ in array1]
        array1.sort()
        array2.sort()
        if array1 == array2:
            return True
        else:
            return False
    except (AttributeError, TypeError):
        return False


# print(comp([2, 3, 4], [16, 4, 9]))
print(comp([]))
