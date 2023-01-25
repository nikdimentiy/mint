# implementation of three common sorting algorithms in computer science, with test-cases for each othe

def insert_sort(A):
    """---insert_sort---"""
    N = len(A)
    for top in range(1, N):
        k = top
        while k > 0 and A[k-1] > A[k]:
            A[k], A[k-1] = A[k-1], A[k]
            k -= 1


def choise_sort(A):
    """---choise_sort---"""
    N = len(A)
    for pos in range(0, N-1):
        for k in range(pos+1, N):
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k]


def bubble_sort(A):
    """---bubble_sort---"""
    N = len(A)
    for bypass in range(1, N):
        for k in range(0, N-bypass):
            if A[k] > A[k+1]:
                A[k], A[k+1] = A[k+1], A[k]


def test_sort(sorting_algorithm):
    print("Testing: ", sorting_algorithm.__doc__)
    print("Testcase #1 ", end=" ")
    A = [4, 2, 5, 1, 3]
    A_sorted = [1, 2, 3, 4, 5]
    sorting_algorithm(A)
    print("Ok" if A == A_sorted else "Fail")

    print("Testcase #2 ", end=" ")
    A = list(range(10, 20)) + list(range(0, 10))
    A_sorted = list(range(20))
    sorting_algorithm(A)
    print("Ok" if A == A_sorted else "Fail")

    print("Testcase #3 ", end=" ")
    A = [4, 2, 4, 2, 1]
    A_sorted = [1, 2, 2, 4, 4]
    sorting_algorithm(A)
    print("Ok" if A == A_sorted else "Fail")
    print()


if __name__ == "__main__":
    test_sort(insert_sort)
    test_sort(choise_sort)
    test_sort(bubble_sort)
