class A:
    """
    This class defines an object that can be initialized with an argument and has a method to return its string representation.
    """
    def __init__(self, arg):
        """
        This method initializes the object with an argument.
        """
        self.arg = arg

    def __str__(self):
        """
        This method returns the string representation of the object.
        """
        return str(self.arg)

class B:
    """
    This class defines an object that can be initialized with a list of arguments and has a method to access elements using indexes.
    """
    def __init__(self, *args):
        """
        This method initializes the object with a list of arguments.
        """
        self.aList = []
        for i in args:
            self.aList.append(i)

    def __getitem__(self, i):
        """
        This method returns the element at the specified index.
        """
        return self.aList[i]

group = B(5, 10, 'abc')
"""
This object is initialized with a list of arguments (5, 10, 'abc').
"""
print(group.aList[1])  # Output: 10
"""
This statement prints the element at index 1 of the 'aList' attribute of the 'group' object.
"""
print(group[0])  # Output: 5
"""
This statement prints the element at index 0 of the 'aList' attribute of the 'group' object.
"""
print(group[2])  # Output: abc
"""
This statement prints the element at index 2 of the 'aList' attribute of the 'group' object.
"""
