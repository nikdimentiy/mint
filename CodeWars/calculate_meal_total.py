def calculate_total(subtotal, tax, tip):
    """
    Calculate the total amount of a restaurant bill.

    Parameters:
    subtotal (float): The initial amount before tax and tip.
    tax (float): The tax percentage to be applied to the subtotal.
    tip (float): The tip percentage to be applied to the subtotal.

    Returns:
    float: The total amount after adding tax and tip, rounded to two decimal places.
    """
    # Calculate the tax amount
    tax_amount = subtotal * tax / 100
    
    # Calculate the tip amount
    tip_amount = subtotal * tip / 100
    
    # Calculate the total by summing the subtotal, tax amount, and tip amount
    total = subtotal + tax_amount + tip_amount
    
    # Return the total rounded to two decimal places
    return round(total, 2)

# Driver code to test the function
if __name__ == "__main__":
    # Example values
    subtotal = 100.00  # Subtotal of the bill
    tax = 8.25        # Tax percentage
    tip = 15.00       # Tip percentage

    # Calculate the total bill
    total_bill = calculate_total(subtotal, tax, tip)

    # Print the result
    print(f"The total bill is: ${total_bill}")
