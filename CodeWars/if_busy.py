def get_status(is_busy):
    """
    Return a dictionary containing the status based on the is_busy parameter.
    
    Args:
        is_busy (bool): A boolean indicating if the status should be busy or available
        
    Returns:
        dict: A dictionary with a single key 'status' whose value is either:
              - 'busy' if is_busy is True
              - 'available' if is_busy is False
              
    Examples:
        >>> get_status(True)
        {'status': 'busy'}
        >>> get_status(False)
        {'status': 'available'}
    """
    # Determine status based on is_busy boolean
    status = "busy" if is_busy else "available"
    
    # Return dictionary with status
    return {"status": status}

# Driver code
def test_get_status():
    # Test case 1: When is_busy is True
    result1 = get_status(True)
    assert result1 == {"status": "busy"}, f"Expected {{'status': 'busy'}}, but got {result1}"
    print("Test 1 passed: Correct status when busy")
    
    # Test case 2: When is_busy is False
    result2 = get_status(False)
    assert result2 == {"status": "available"}, f"Expected {{'status': 'available'}}, but got {result2}"
    print("Test 2 passed: Correct status when available")
    
    # Test case 3: Check return type is dictionary
    result3 = get_status(True)
    assert isinstance(result3, dict), f"Expected dict type, but got {type(result3)}"
    print("Test 3 passed: Return type is dictionary")
    
    print("All tests passed!")

if __name__ == "__main__":
    # Run the tests
    test_get_status()
    
    # Example usage
    print("\nExample usage:")
    print(f"Status when busy: {get_status(True)}")
    print(f"Status when available: {get_status(False)}")
