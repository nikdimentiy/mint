class EvenLengthMixin:
    """
    This mixin class provides a method to check if the length of a list is even.
    """

    def even_length(self) -> bool:
        """
        Checks if the length of the list is even.

        Returns:
            True if the length of the list is even, False otherwise.
        """
        return len(self) % 2 == 0  # Check if the length of the list is even using the modulo operator

class MyList(list, EvenLengthMixin):
    """
    This class inherits from the `list` class and adds a method to check if the length of the list is even.
    """

    def pop(self):
        """
        Pops the last element from the list and prints a message indicating the popped value.

        Returns:
            The popped value.
        """
        x = list.pop(self)  # Pop the last element from the list
        print("Last value is", x)  # Print a message indicating the popped value
        return x

# Driver code
mylist = MyList([1, 2, 3, 4])  # Create an instance of the MyList class with an initial list of [1, 2, 3, 4]
print(mylist.even_length())  # Check if the length of the list is even
print(mylist.pop())  # Pop the last element from the list
print(mylist)  # Print the remaining list
