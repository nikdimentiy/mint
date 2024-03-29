from array_search import array_search


def test_array_search():
    A1 = [1, 2, 3, 4, -1]
    res = array_search(A1, 5, -1)
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

    A3 = [10, 20, 30, 20, 40, 50]
    res = array_search(A3, 6, 30)
    if res == 2:
        print("#3. Test - OK")
    else:
        print("#3. Test - Fail")
