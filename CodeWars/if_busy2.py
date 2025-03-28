def get_status(is_busy):
    """
    Generate a status dictionary based on the busy state.

    This function creates a dictionary with a 'status' key whose value 
    depends on the truth value of the input argument. It uses a concise 
    approach with tuple indexing and the 'not' operator to handle 
    different input types.

    Args:
        is_busy (bool or any): Input value to determine status
                                Truthy values result in "busy"
                                Falsy values result in "available"

    Returns:
        dict: A dictionary with 'status' key 
              Value is either "busy" or "available"

    Examples:
        >>> get_status(True)
        {'status': 'busy'}
        >>> get_status(False)
        {'status': 'available'}
        >>> get_status(1)
        {'status': 'busy'}
        >>> get_status(0)
        {'status': 'available'}
    """
    # Use tuple indexing with 'not' to convert truthy/falsy values to status
    # 'not is_busy' will be True for falsy values, False for truthy values
    return {"status": ("busy", "available")[not is_busy]}

# Driver code to demonstrate the function
def main():
    # Test cases to show different input types
    test_cases = [
        True,       # Boolean True
        False,      # Boolean False
        1,          # Integer truthy value
        0,          # Integer falsy value
        "hello",    # Truthy string
        "",         # Falsy string
        None,       # Falsy None
        []          # Falsy empty list
    ]
    
    # Run tests and print results
    for case in test_cases:
        result = get_status(case)
        print(f"Input: {case}")
        print(f"Status: {result}\n")

# Ensure the script can be run directly or imported as a module
if __name__ == "__main__":
    main()
