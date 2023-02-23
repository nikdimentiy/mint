# How to take the determinant of a matrix -- it is simplest to start with the smallest cases:

# A 1x1 matrix |a| has determinant a.

# A 2x2 matrix [ [a, b], [c, d] ]

import numpy as np


def determinant(a):
    return round(np.linalg.det(np.matrix(a)))
