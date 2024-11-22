import operator

# Sample data for demonstration purposes
A001055 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

def inf_database(range_, str_, val):
    """
    Filters the global list A001055 based on a specified condition.

    Parameters:
    range_ (tuple): A tuple containing the start and end indices (inclusive) for filtering.
    str_ (str): A string representing the condition to apply. 
                Options include: "higher than", "higher and equals to", 
                "equals to", "lower than", "lower and equals to".
    val (int or float): The value to compare against the elements in A001055.

    Returns:
    tuple: A tuple containing the count of elements that meet the condition 
           and a list of those elements. If the condition string is invalid, 
           returns "wrong constraint".
    """
    global A001055
    # Dictionary mapping condition strings to their corresponding operator functions
    s = {
        "higher than": operator.gt,
        "higher and equals to": operator.ge,
        "equals to": operator.eq,
        "lower than": operator.lt,
        "lower and equals to": operator.le
    }

    # Check if the provided condition string is valid
    if str_ in s:
        # Create a list of elements that satisfy the condition
        l = [i for i in range(range_[0], range_[1] + 1)
             if s[str_](A001055[i], val)]
        return (len(l), l)
    else:
        return "wrong constraint"

# Driver code to demonstrate the usage of inf_database function
if __name__ == "__main__":
    # Define the range and condition
    range_ = (0, 9)  # Indices from 0 to 9 (inclusive)
    condition = "higher than"
    value = 50

    # Call the function and print the result
    result = inf_database(range_, condition, value)
    print(f"Condition: '{condition}' with value {value} in range {range_} -> Result: {result}")

    # Test with another condition
    condition = "lower and equals to"
    value = 30
    result = inf_database(range_, condition, value)
    print(f"Condition: '{condition}' with value {value} in range {range_} -> Result: {result}")

    # Test with an invalid condition
    condition = "not a valid condition"
    result = inf_database(range_, condition, value)
    print(f"Condition: '{condition}' with value {value} in range {range_} -> Result: {result}")
