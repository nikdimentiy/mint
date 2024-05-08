# Solution 1
def is_anagram(test, original):
    """
    Check if two given strings are anagrams of each other.

    Args:
        test (str): The first string to be checked.
        original (str): The second string to be checked.

    Returns:
        bool: True if the strings are anagrams, False otherwise.
    """
    # Convert both strings to lowercase
    test_lower = test.lower()
    original_lower = original.lower()

    # Convert strings to sets to remove duplicates
    test_set = set(test_lower)
    original_set = set(original_lower)

    # Check if the sets are equal (anagram condition 1)
    anagram_condition_1 = test_set == original_set

    # Check if the lengths are equal (anagram condition 2)
    anagram_condition_2 = len(test) == len(original)

    # Return True if both conditions are met, False otherwise
    return anagram_condition_1 and anagram_condition_2

# Solution 2
def is_anagram(test, original):
    """
    Check if two given strings are anagrams of each other.

    Args:
        test (str): The first string to be checked.
        original (str): The second string to be checked.

    Returns:
        bool: True if the strings are anagrams, False otherwise.
    """
    # Convert both strings to lowercase
    test_lower = test.lower()
    original_lower = original.lower()

    # Sort the characters in both strings
    sorted_test = sorted(test_lower)
    sorted_original = sorted(original_lower)

    # Check if the sorted strings are equal
    return sorted_test == sorted_original

# Driver code
test_string_1 = "listen"
original_string_1 = "silent"

test_string_2 = "hello"
original_string_2 = "world"

print("Solution 1:")
print(f"'{test_string_1}' and '{original_string_1}' are anagrams: {is_anagram(test_string_1, original_string_1)}")
print(f"'{test_string_2}' and '{original_string_2}' are anagrams: {is_anagram(test_string_2, original_string_2)}")

print("\nSolution 2:")
print(f"'{test_string_1}' and '{original_string_1}' are anagrams: {is_anagram(test_string_1, original_string_1)}")
print(f"'{test_string_2}' and '{original_string_2}' are anagrams: {is_anagram(test_string_2, original_string_2)}")
