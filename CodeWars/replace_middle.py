# We define the middle of the array arr as follows:

# if arr contains an odd number of elements, its middle is the element whose index number is the same
# when counting from the beginning of the array and from its end;
# if arr contains an even number of elements, its middle is the sum of the two elements
# whose index numbers when counting from the beginning and from the end of the array differ by one.
# Given array arr, your task is to find its middle, and, if it consists of two elements,
# replace those elements with the value of middle. Return the resulting array as the answer.


def solution(arr):
    length = len(arr)
    if length % 2 == 0:
        # even length array
        middle_idx1 = length // 2 - 1
        middle_idx2 = middle_idx1 + 1
        middle = arr[middle_idx1] + arr[middle_idx2]
        arr[middle_idx1:middle_idx2+1] = [middle]
    else:
        # odd length array
        middle_idx = length // 2
        arr[middle_idx] = arr[middle_idx]
    return arr
