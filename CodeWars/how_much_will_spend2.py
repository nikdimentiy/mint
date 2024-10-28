def getTotal(costs, items, tax):
    """
    Calculate the total cost of items including tax.

    Parameters:
    costs (dict): A dictionary where keys are item names and values are their costs.
    items (list): A list of item names to be purchased.
    tax (float): The tax rate to be applied (e.g., 0.07 for 7% tax).

    Returns:
    float: The total cost of the items including tax, rounded to two decimal places.
    """
    
    # Calculate the subtotal by summing the costs of the specified items
    subtotal = sum([costs.get(i, 0) for i in items])
    
    # Calculate the total by applying the tax rate to the subtotal
    total = subtotal * (1 + tax)
    
    # Return the total cost rounded to two decimal places
    return round(total, 2)

# Driver code to test the getTotal function
if __name__ == "__main__":
    # Sample costs dictionary
    costs = {
        "apple": 0.50,
        "banana": 0.30,
        "orange": 0.80,
        "grape": 1.00
    }
    
    # List of items to purchase
    items = ["apple", "banana", "grape"]
    
    # Tax rate (e.g., 7%)
    tax = 0.07
    
    # Calculate the total cost
    total_cost = getTotal(costs, items, tax)
    
    # Print the result
    print(f"The total cost of the items is: ${total_cost}")
