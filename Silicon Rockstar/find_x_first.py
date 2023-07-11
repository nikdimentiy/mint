# define the findx function
def findx(seq, x):
    """This function takes a sequence (seq) and a value (x) as input and returns the index of the first occurrence of x in seq, or -1 if x is not in seq."""

    # initialize ans to -1, which means x is not found yet
    ans = -1

    # loop through the sequence from left to right
    for i in range(len(seq)):

        # check if the current element is equal to x and ans is still -1
        if ans == -1 and seq[i] == x:

            # update ans to the current index
            ans = i

    # return the final answer
    return ans


# define some test cases to check if the function works correctly
test_cases = [
    ([1, 2, 3, 4, 5], 3, 2),  # x is in the middle of seq
    ([1, 2, 3, 4, 5], 6, -1),  # x is not in seq
    ([1, 2, 3, 4, 5], 1, 0),   # x is the first element of seq
    ([], 5, -1)                # seq is empty
]

# run the test cases
for seq, x, expected_output in test_cases:

    # call the findx function and store the output
    output = findx(seq, x)

    # compare the output with the expected output and print the result
    if output == expected_output:
        print(f"findx({seq}, {x}) = {output} (CORRECT)")
    else:
        print(
            f"findx({seq}, {x}) = {output}, but expected {expected_output} (INCORRECT)")
