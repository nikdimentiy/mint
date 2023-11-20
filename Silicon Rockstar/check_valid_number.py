class Natural:
    """
    This class represents a natural number. A natural number is a positive integer.

    Attributes:
        __origin (int): The original value of the natural number.
        number (int): The converted value of the natural number.
    """
    def __init__(self, n):
        """
        Constructs a Natural object.

        Args:
            n (int): The value of the natural number.
        """
        self.__origin = n
        self.number = self.__test()

    def __test(self):
        """
        Tests if the value of the natural number is valid. A valid natural number is a positive integer.

        Returns:
            int: The converted value of the natural number. If the original value is not a valid natural number, it is converted to 1.
        """
        if type(self.__origin) is int and self.__origin > 0:
            return self.__origin
        else:
            print(f"Value {self.__origin} was converted to 1")
            return 1

a = Natural(34)
b = Natural(-250)
c = Natural("Hello")

print(a.number, b.number, c.number)
