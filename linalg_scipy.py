"""

Linear Algebra (scipy.linalg)
    SciPy extends NumPy’s linear algebra (numpy.linalg) with additional features.

🔹 Solving a System of Equations
    Solve this system:

        3x+2y=5
        4x+5y=6


"""

import numpy as np
from scipy.linalg import solve

# Coefficients matrix
A = np.array([[3, 2], [4, 5]])

# Constants
B = np.array([5, 6])

# Solve for x and y
solution = solve(A, B)
print("Solution (x, y):", solution)


"""
#output :
    Solution (x, y): [ 1.85714286 -0.28571429]

"""


# Finding Determinant
from scipy.linalg import det

A = np.array([[3, 2], [4, 5]])
print("Determinant:", det(A))

"""
#output :
    Determinant: 7.0

"""



