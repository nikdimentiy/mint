class Block(object):
    """
    A class to represent a 3D block.

    Attributes:
    width (int): The width of the block.
    length (int): The length of the block.
    height (int): The height of the block.

    Methods:
    get_width(): Returns the width of the block.
    get_length(): Returns the length of the block.
    get_height(): Returns the height of the block.
    get_volume(): Returns the volume of the block.
    get_surface_area(): Returns the surface area of the block.
    """

    def __init__(self, arr):
        """
        Initializes a Block instance with the given dimensions.

        Parameters:
        arr (list): A list containing three integers [width, length, height].
        """
        self.width = arr[0]   # Set the width from the first element of the array
        self.length = arr[1]  # Set the length from the second element of the array
        self.height = arr[2]  # Set the height from the third element of the array

    def get_width(self):
        """Returns the width of the block."""
        return self.width

    def get_length(self):
        """Returns the length of the block."""
        return self.length

    def get_height(self):
        """Returns the height of the block."""
        return self.height

    def get_volume(self):
        """Calculates and returns the volume of the block."""
        return self.width * self.length * self.height

    def get_surface_area(self):
        """Calculates and returns the surface area of the block."""
        return (self.width * self.length * 2 + 
                self.width * self.height * 2 + 
                self.length * self.height * 2)


# Driver code to demonstrate the usage of the Block class
if __name__ == "__main__":
    # Create a block with dimensions width=3, length=4, height=5
    dimensions = [3, 4, 5]
    block = Block(dimensions)

    # Print the dimensions of the block
    print("Width:", block.get_width())
    print("Length:", block.get_length())
    print("Height:", block.get_height())

    # Print the volume of the block
    print("Volume:", block.get_volume())

    # Print the surface area of the block
    print("Surface Area:", block.get_surface_area())
