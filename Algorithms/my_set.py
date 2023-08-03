"""
This Python code implements a simple hash set using a nested list.

The doc string provides a brief description of the code and its functions.
The comments in the code provide more detailed explanations of what the code is doing.

The code is runnable and can get execution results.
The code does not read file or ask for input.
"""

setsize = 10
myset = [[] for _ in range(setsize)]


def add(x):
    """
    Add an element to the hash set.

    Args:
        x: The element to add.

    Returns:
        None.

    Comments:
        Append the element to the list at the index corresponding to the element's hash value.
    """

    myset[x % setsize].append(x)


def find(x):
    """
    Search for an element in the hash set.

    Args:
        x: The element to search for.

    Returns:
        True if the element is found, False otherwise.

    Comments:
        Iterate over the list at the index corresponding to the element's hash value and return True if the element is found.
    """

    for now in myset[x % setsize]:
        if now == x:
            return True
    return False


def delete(x):
    """
    Delete an element from the hash set.

    Args:
        x: The element to delete.

    Returns:
        None.

    Comments:
        Find the element in the list at the index corresponding to the element's hash value and remove it from the list.
    """

    xlist = myset[x % setsize]
    for i in range(len(xlist)):
        if xlist[i] == x:
            xlist[i] = xlist[len(xlist) - 1]
            xlist.pop()
            return


if __name__ == "__main__":
    add(10)
    add(20)
    add(30)
    print(find(10))  # True
    print(find(20))  # True
    print(find(30))  # True
    delete(20)
    print(find(20))  # False

