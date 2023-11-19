class Table:
    """
    This class represents a table with a specified length, width, and height.
    """

    def __init__(self, l=1, w=1, h=1):
        """
        This method initializes the Table object with the specified length, width, and height.
        """
        self.length = l  # The length of the table
        self.width = w  # The width of the table
        self.height = h  # The height of the table

class KitchenTable(Table):
    """
    This class represents a kitchen table, which is a type of table that also has a specified number of seats.
    """

    def __init__(self, l=1, w=1, h=1):
        """
        This method initializes the KitchenTable object with the specified length, width, height, and number of seats.
        """
        super().__init__(l, w, h)  # Call the parent class's constructor to initialize the table dimensions
        p = int(input("How many seats: "))  # Get the number of seats from the user
        self.places = p  # Set the number of seats attribute

# Creating objects of the Table and KitchenTable classes
table = Table()  # Create a Table object with default dimensions
kitchen_table = KitchenTable()  # Create a KitchenTable object with default dimensions

# Printing the dimensions of the table
print(f"Table dimensions: {table.length} x {table.width} x {table.height}")  # Print the table dimensions

# Printing the dimensions and number of seats of the kitchen table
print(f"Kitchen table dimensions: {kitchen_table.length} x {kitchen_table.width} x {kitchen_table.height}")  # Print the kitchen table dimensions
print(f"Number of seats: {kitchen_table.places}")  # Print the number of seats
