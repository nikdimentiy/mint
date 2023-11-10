class DoubleElementListIterator:
    def __init__(self, lst):
        """
        Initializes the iterator with a list and sets the starting index to 0.

        Args:
        - lst: The list to iterate over.
        """
        self.lst = lst
        self.i = 0

    def __next__(self):
        """
        Returns the next pair of elements in the list.

        Returns:
        - A tuple containing the current and next element in the list.

        Raises:
        - StopIteration: If there are no more pairs of elements in the list.
        """
        if self.i < len(self.lst):
            result = (self.lst[self.i - 2], self.lst[self.i - 1])
            self.i += 2
            return result
        else:
            raise StopIteration

class MyList(list):
    def __iter__(self):
        """
        Returns an instance of DoubleElementListIterator to iterate over the list.

        Returns:
        - An iterator object for iterating over the list.
        """
        return DoubleElementListIterator(self)
