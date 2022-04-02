def array_search(A: list, N: int, x: int) -> int:
    """Some document string"""
    pass


def test_array_search():
    A1 = [1, 2, 3, 4, 5]
    m = array_search(A1, 5, 8)
    if m == -1:
        print("#1. Test - OK")
    else:
        print("#1. Test - Fail")

    A2 = [-1, -2, -3, -4, -5]
    m = array_search(A1, 5, -3)
    if m == 2:
        print("#2. Test - OK")
    else:
        print("#2. Test - Fail")

    A3 = [10, 20, 30, 20, 40]
    m = array_search(A1, 5, 20)
    if m == 1:
        print("#3. Test - OK")
    else:
        print("#3. Test - Fail")

