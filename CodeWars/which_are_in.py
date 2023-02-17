# Given two arrays of strings a1 and a2 return a sorted array r in lexicographical order
# of the strings of a1 which are substrings of strings of a2.

# Example 1:
# a1 = ["arp", "live", "strong"]

# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

# returns ["arp", "live", "strong"]

# Example 2:
# a1 = ["tarp", "mice", "bull"]

# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

# returns []


def in_array(array1, array2):
    # initialize an empty list to store the result
    result = []
    # loop through each string in a1
    for s1 in array1:
        # loop through each string in a2
        for s2 in array2:
            # check if s1 is a substring of s2
            if s1 in s2:
                # add s1 to the result list if not already present
                if s1 not in result:
                    result.append(s1)
                # break the inner loop as we only need one match
                break
    # sort the result list lexicographically using sorted function
    result = sorted(result)
    # return the result list
    return result


# test the function with given examples
a1 = ["arp", "live", "strong"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
print(in_array(a1, a2))  # prints ["arp", "live", "strong"]

a1 = ["tarp", "mice", "bull"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
print(in_array(a1, a2))  # prints []
