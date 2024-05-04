class MenuItem:
    """Models each individual item on the coffee menu, including its name, ingredients, and cost."""
    
    def __init__(self, name, water, milk, coffee, cost):
        # Initialize the name, cost, and ingredient requirements for the menu item
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,  # Amount of water required for this menu item
            "milk": milk,  # Amount of milk required for this menu item
            "coffee": coffee  # Amount of coffee required for this menu item
        }


class Menu:
    """Represents the coffee machine's menu, which contains multiple drink items."""
    
    def __init__(self):
        # Create a list of predefined menu items available for ordering
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self):
        """Returns a string with the names of all available menu items, separated by slashes."""
        options = "/".join([item.name for item in self.menu])  # Concatenate all item names with a slash separator
        return options

    def find_drink(self, order_name):
        """
        Searches the menu for a particular drink by its name.
        Returns the corresponding MenuItem object if found.
        If the drink does not exist, prints a message and returns None.
        """
        # Loop through the menu to find a matching item
        for item in self.menu:
            if item.name.lower() == order_name.lower():  # Case-insensitive comparison for better user experience
                return item  # Return the matching menu item

        # If no item matches, print a message and return None
        print("Sorry, that item is not available.")
        return None
