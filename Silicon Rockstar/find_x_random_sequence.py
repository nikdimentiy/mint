import random

def find_x(seq, x):
    """
    Find the index of the first occurrence of x in seq.

    Parameters:
    seq (list): A list of elements to search through.
    x (any): The element to search for.

    Returns:
    int: The index of the first occurrence of x in seq, or -1 if x is not found.
    """
    ans = -1
    for i in range(len(seq)):
        if seq[i] == x:
            ans = i
            break
    return ans

# User input
element = int(input("Enter the element you want to search for: "))

# Generate random sequence
sequence = random.sample(range(1, 101), 15)

# Display the randomly generated sequence
print("Randomly generated sequence:")
print(sequence)

# Find the element in the sequence
result = find_x(sequence, element)

# Display the result
if result != -1:
    print(f"Element {element} found at index {result}.")
else:
    print(f"Element {element} not found in the sequence.")
