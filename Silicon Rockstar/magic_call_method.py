class Changeable:
    """
    This class is used to create objects that can change their color.
    """
    def __init__(self, color):
        """
        This method initializes the object with a color.
        """
        self.color = color

    def __call__(self, newcolor):
        """
        This method changes the color of the object.
        """
        self.color = newcolor

    def __str__(self):
        """
        This method returns the color of the object as a string.
        """
        return "%s" % self.color

canvas = Changeable("green")
"""
This object is initialized with the color green.
"""
frame = Changeable("blue")
"""
This object is initialized with the color blue.
"""
canvas("red")
"""
This method changes the color of the canvas object to red.
"""
frame("yellow")
"""
This method changes the color of the frame object to yellow.
"""
print(canvas, frame)
"""
This prints the color of the canvas object and the color of the frame object.
"""
