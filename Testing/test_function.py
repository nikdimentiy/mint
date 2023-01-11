def insert_sort(A):
    """insert sort array (list)"""
    pass


def select_sort(A):
    """select sort array (list)"""
    pass


def bubble_sort(A):
    """bubble sort array (list)"""
    pass


def test_sort(sort_algorithm):
    print("🔥 Now working:-->", sort_algorithm.__doc__)
    print("Test_case : ", end="")
    A = [4, 2, 5, 1, 3]
    A_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(A)
    print("✅Ok" if A == A_sorted else "❌Fail")

    print("Test case #2: ", end="")
    A = list(range(10, 20)) + list(range(0, 10))
    A_sorted = list(range(20))
    sort_algorithm(A)
    print("✅Ok" if A == A_sorted else "❌Fail")

    print("Test case #3: ", end="")
    A = [4, 2, 4, 3, 1]
    A_sorted = [1, 2, 3, 4, 4]
    sort_algorithm(A)
    print("✅Ok" if A == A_sorted else "❌Fail")


if __name__ == "__main__":
    test_sort(insert_sort)
    test_sort(select_sort)
    test_sort(bubble_sort)
