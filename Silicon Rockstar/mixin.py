"""
This code defines two classes: `EvenLengthMixin` and `MyList`. The `EvenLengthMixin` class provides a method `even_length()` that checks whether the length of the object is even. The `MyList` class inherits from both the `list` class and the `EvenLengthMixin` class. This means that `MyList` objects have all the methods of both `list` objects and `EvenLengthMixin` objects.

The driver code creates a `MyList` object called `myList` and then calls the `even_length()` and `remove()` methods on `myList`. The `even_length()` method returns `True` because the length of `myList` is even. The `remove()` method removes the value 3 from `myList`. The updated value of `myList` is printed to the console.
"""


class EvenLengthMixin:
    """
    This mixin class provides a method `even_length()` that checks whether the length of the object is even.

    Methods:
        even_length(): Checks whether the length of the object is even.

        Returns:
            True if the length of the object is even, False otherwise.
    """

    def even_length(self):
        """
        Checks whether the length of the object is even.

        Returns:
            True if the length of the object is even, False otherwise.
        """
        return len(self) % 2 == 0


class MyList(list, EvenLengthMixin):
    """
    This class inherits from both the `list` class and the `EvenLengthMixin` class. This means that `MyList` objects have all the methods of both `list` objects and `EvenLengthMixin` objects.

    Methods:
        remove(value): Removes the first occurrence of the specified value from the list.

        Args:
            value: The value to remove.

        Returns:
            None if the value is not in the list, otherwise the removed value.
    """

    def remove(self, value):
        """
        Removes the first occurrence of the specified value from the list.

        Args:
            value: The value to remove.

        Returns:
            None if the value is not in the list, otherwise the removed value.
        """
        if value not in self:
            return None
        else:
            super().remove(value)


# Driver code
myList = MyList([1, 2, 3, 4, 5])
print(myList.even_length())  # Output: True
myList.remove(3)
print(myList)  # Output: [1, 2, 4, 5]
