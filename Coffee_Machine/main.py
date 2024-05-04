# Import necessary classes
from menu import Menu  # Provides the menu of drinks
from coffee_maker import CoffeeMaker  # Handles coffee-making process
from money_machine import MoneyMachine  # Deals with money transactions

"""
This script simulates a coffee machine. It allows a user to:
- Request a report on the machine's status (resources and money).
- Order a drink from a menu of coffee drinks.
- Turn off the machine.

The coffee machine operates until the user decides to turn it off.
It checks for sufficient resources and processes payment before making a drink.
"""


# Initialize the machines and menu
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

# This variable controls whether the coffee machine is running
is_on = True

# Loop to keep the coffee machine operational
while is_on:
    # Get the list of available drink options
    options = menu.get_items()

    # Prompt the user to choose a drink or perform an action
    choice = input(f"What would you like? ({options}): ")

    # Exit condition to turn off the coffee machine
    if choice.lower() == "off":
        is_on = False  # Turn off the machine
    # Display a report of current resources and money status
    elif choice.lower() == "report":
        coffee_maker.report()  # Display the status of coffee resources
        money_machine.report()  # Display the status of money

    # If the user selects a drink from the menu
    else:
        # Find the corresponding drink object
        drink = menu.find_drink(choice)

        # Check if the required resources are available for the selected drink
        if coffee_maker.is_resource_sufficient(drink):
            # Attempt to process the payment for the drink
            if money_machine.make_payment(drink.cost):
                # Make the coffee if payment is successful
                coffee_maker.make_coffee(drink)
