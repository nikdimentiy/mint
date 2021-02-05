# solution of problem: Tower of Hanoi

def hanoi(n, a, b, c):
    """param n:  number of rings
       param a:  first kernel
       param b:  second kernel
       param c:  third kernel
    """
    if n != 0:  # if the number of rings is not zero - move n-1 rings from A to B
        hanoi(n - 1, a, c, b)
        # move one ring from A to C
        print("Move the ring from", a, "to", c)
        # move n-1 rings from B to C
        hanoi(n - 1, b, a, c)


n = int(input("Enter the positive integer - number of needed rings: "))
hanoi(n, 'A', 'B', 'C')
