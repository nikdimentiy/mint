# Define the insertion sort function with a docstring.
def insert_sort(A):
    """Insertion sort for an array (list)"""
    N = len(A)
    for top in range(1, N):
        k = top
        while k > 0 and A[k - 1] > A[k]:
            # Swap elements if they are out of order.
            A[k], A[k - 1] = A[k - 1], A[k]
            k -= 1

# Define the selection sort function with a docstring.
def select_sort(A):
    """Selection sort for an array (list)"""
    N = len(A)
    for pos in range(0, N - 1):
        for k in range(pos + 1, N):
            if A[k] < A[pos]:
                # Swap elements to move the smallest one to the front.
                A[k], A[pos] = A[pos], A[k]

# Define the bubble sort function with a docstring.
def bubble_sort(A):
    """Bubble sort for an array (list)"""
    N = len(A)
    for bypass in range(1, N):
        for k in range(0, N - bypass):
            if A[k] > A[k + 1]:
                # Swap elements if they are out of order.
                A[k], A[k + 1] = A[k + 1], A[k]

# Define a function for testing the sorting algorithms.
def test_sort(sort_algorithm):
    # Print the name of the sorting algorithm being tested.
    print("🔥 Now working:-->", sort_algorithm.__doc__)
    
    # Test case #1
    print("Test_case #1: ", end="")
    A = [4, 2, 5, 1, 3]
    A_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(A)
    # Check if the array is correctly sorted and print the result.
    print("✅Ok" if A == A_sorted else "❌Fail")

    # Test case #2
    print("Test case #2: ", end="")
    A = list(range(10, 20)) + list(range(0, 10))
    A_sorted = list(range(20)
    sort_algorithm(A)
    # Check if the array is correctly sorted and print the result.
    print("✅Ok" if A == A_sorted else "❌Fail")

    # Test case #3
    print("Test case #3: ", end="")
    A = [4, 2, 4, 3, 1]
    A_sorted = [1, 2, 3, 4, 4]
    sort_algorithm(A)
    # Check if the array is correctly sorted and print the result.
    print("✅Ok" if A == A_sorted else "❌Fail")

# Execute the testing code when the script is run.
if __name__ == "__main__":
    test_sort(insert_sort)    # Test the insertion sort algorithm
    test_sort(select_sort)    # Test the selection sort algorithm
    test_sort(bubble_sort)    # Test the bubble sort algorithm
