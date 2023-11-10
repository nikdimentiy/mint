class DoubleElementListIterator:
    def __init__(self, lst):
        self.lst = lst
        self.i = 0

    def __next__(self):
        if self.i < len(self.lst):
            result = (self.lst[self.i - 2], self.lst[self.i - 1])
            self.i += 2
            return result
        else:
            raise StopIteration

class MyList(list):
    def __iter__(self):
        return DoubleElementListIterator(self)

# Example usage
my_list = MyList([1, 2, 3, 4, 5, 6])
for pair in my_list:
    print(pair)
