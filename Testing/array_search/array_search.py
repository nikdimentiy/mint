def array_search(A: list, N: int, x: int):
    """This function does search for a number X in the array A from zero to the last 
       index inclusive.
       Returns the index of an element in the array or -1, if the number is not in the array.
    """
    for k in range(len(A)):
        if A[k] == x and len(A) == N:
            return k
    if len(A) != N:
        return None
    return - 1
