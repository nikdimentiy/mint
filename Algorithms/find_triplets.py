def find_triplets(arr):
    """
    This function finds all triplets in the given array whose sum is zero.

    Args:
        arr: The array of numbers.

    Returns:
        A list of all triplets whose sum is zero.
    """

    n = len(arr)
    hash_table = {}
    for i in range(n):
        hash_table[arr[i]] = i

    triplets = []
    for i in range(n):
        for j in range(i + 1, n):
            target = -arr[i] - arr[j]
            if target in hash_table:
                k = hash_table[target]
                if k > j:
                    triplets.append([arr[i], arr[j], arr[k]])

    return triplets


# This is a sample array
arr = [0, -1, 2, -3, 1]

# Find all triplets in the array
triplets = find_triplets(arr)

# Print the triplets
print(triplets)
