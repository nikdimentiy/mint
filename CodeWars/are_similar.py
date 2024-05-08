def solution(a, b):
    """
    Determine if two strings are anagrams of each other with at most two differences.

    Args:
        a (str): The first string.
        b (str): The second string.

    Returns:
        bool: True if the strings are anagrams with at most two differences, False otherwise.
    """
    # Check if the sorted strings are different
    if sorted(a) != sorted(b):
        # If sorted strings are different, they cannot be anagrams
        return False

    # Count the number of differences between the strings
    count = 0
    for i in range(len(a)):
        # Check if the characters at the same position are different
        if a[i] != b[i]:
            count += 1

    # If the count of differences is less than or equal to 2, return True, else False
    return count <= 2

# Driver code
print(solution("anagram", "nagaram"))  # True
print(solution("anagram", "nagaram"))  # False
print(solution("hello", "hello"))  # True
print(solution("hello", "world"))  # False
