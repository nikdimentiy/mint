# In your class, you have started lessons about arithmetic progression. Since you are also a programmer,
# you have decided to write a function that will return the first n elements of the sequence
# with the given common difference d and first element a. Note that the difference may be zero!

# The result should be a string of numbers, separated by comma and space.


def arithmetic_sequence_elements(a, d, n):
    sequence = []  # create an empty list to store sequence elements
    for i in range(n):
        # append each element to the sequence list as a string
        sequence.append(str(a + (i * d)))
    # join sequence elements into a string separated by comma and space
    return ", ".join(sequence)


print(arithmetic_sequence_elements(1, 2, 5))  # output: "1, 3, 5, 7, 9"
print(arithmetic_sequence_elements(0, 0, 5))  # output: "0, 0, 0, 0, 0"
print(arithmetic_sequence_elements(3, -1, 5))  # output: "3, 2, 1, 0, -1"
