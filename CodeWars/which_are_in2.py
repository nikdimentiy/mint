def in_array(a1, a2):
    """
    Returns a sorted array of unique strings from a1 that are substrings of any string in a2.

    Parameters:
    a1 (list of str): The first array of strings to check for substrings.
    a2 (list of str): The second array of strings to check against.

    Returns:
    list of str: A sorted list of unique strings from a1 that are found as substrings in a2.
    
    Example:
    >>> in_array(["arp", "live", "strong"], ["lively", "alive", "harp", "sharp", "armstrong"])
    ['arp', 'live', 'strong']
    
    >>> in_array(["tarp", "mice", "bull"], ["lively", "alive", "harp", "sharp", "armstrong"])
    []
    """
    # Use a set comprehension to find unique substrings from a1 that are in any string of a2
    return sorted({sub for sub in a1 if any(sub in s for s in a2)})

# Driver code to test the function
if __name__ == "__main__":
    # Test case 1
    a1 = ["arp", "live", "strong"]
    a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
    result = in_array(a1, a2)
    print(f"Result for a1={a1} and a2={a2}: {result}")  # Expected: ['arp', 'live', 'strong']

    # Test case 2
    a1 = ["tarp", "mice", "bull"]
    a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
    result = in_array(a1, a2)
    print(f"Result for a1={a1} and a2={a2}: {result}")  # Expected: []
