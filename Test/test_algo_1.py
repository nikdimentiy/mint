import pytest
from algo_1 import findmax

# Test case for an empty sequence
def test_findmax_empty_sequence():
    sequence = []
    with pytest.raises(ValueError):
        findmax(sequence)

# Test case for a sequence with one element
def test_findmax_single_element_sequence():
    sequence = [5]
    with pytest.raises(ValueError):
        findmax(sequence)

# Test case for a sequence with two elements in ascending order
def test_findmax_two_elements_ascending():
    sequence = [3, 7]
    assert findmax(sequence) == (7, 3)

# Test case for a sequence with two elements in descending order
def test_findmax_two_elements_descending():
    sequence = [9, 2]
    assert findmax(sequence) == (9, 2)

# Test case for a sequence with multiple elements
def test_findmax_multiple_elements():
    sequence = [4, 2, 9, 6, 1, 8]
    assert findmax(sequence) == (9, 8)

# Test case for a sequence with repeated elements
def test_findmax_repeated_elements():
    sequence = [4, 2, 9, 6, 9, 8]
    assert findmax(sequence) == (9, 9)

# Test case for a sequence with negative elements
def test_findmax_negative_elements():
    sequence = [-5, -2, -9, -6, -1, -8]
    assert findmax(sequence) == (-1, -2)
