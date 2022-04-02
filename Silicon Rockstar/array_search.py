def array_search(A: list, N: int, x: int) -> int:
    """This function does search for a number X in the array A from zero to the last index inclusive.
       Returns the index of an element in the array or -1, if the number is not in the array.
       If there are several identical elements equal to X in the array A, 
       the function return the index of the first position of element X """
    for k in range(N):
        if A[k] == x:
            return k
    return - 1


def test_array_search():
    A1 = [1, 2, 3, 4, 5]
    res = array_search(A1, 5, 8)
    if res == -1:
        print("#1. Test - OK")
    else:
        print("#1. Test - Fail")

    A2 = [-1, -2, -3, -4, -5]
    res = array_search(A2, 5, -3)
    if res == 2:
        print("#2. Test - OK")
    else:
        print("#2. Test - Fail")

    A3 = [10, 20, 30, 20, 40]
    m = array_search(A3, 5, 20)
    if res == 1:
        print("#3. Test - OK")
    else:
        print("#3. Test - Fail")


test_array_search()

