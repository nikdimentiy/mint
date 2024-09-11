def findNeedle(haystack: list) -> str:
    """
    Find the position of the "needle" in the haystack.

    Args:
        haystack (list): A list of strings to search through.

    Returns:
        str: A message indicating the position of the "needle" if found.
        None: If the "needle" is not found in the haystack.
    """
    # Iterate through the haystack to find the needle
    for index, item in enumerate(haystack):
        # Check if the current item is the "needle"
        if item == "needle":
            # Return the position of the needle
            return f"found the needle at position {index}"
    
    # If the loop completes without finding the needle, return None
    return None

# Driver code
if __name__ == "__main__":
    # Example usage
    haystack = ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]
    result = findNeedle(haystack)
    print(result)  # Output: "found the needle at position 5"

    # Additional test cases
    print(findNeedle(["needle", "hay", "hay"]))  # Output: "found the needle at position 0"
    print(findNeedle(["hay", "hay", "hay"]))  # Output: None