"""

ptimization (scipy.optimize)
Optimization is used to find the minimum or maximum of a function.

🔹 Finding the Minimum of a Function
Let’s minimize 

f(x)=x 2+3x+2.

"""


from scipy.optimize import minimize

# Function to minimize
def f(x):
    return x**2 + 3*x + 2

# Initial guess
x0 = 0

# Minimize function
result = minimize(f, x0)
print("Minimum value:", result.x)

#out put : Minimum value: [-1.50000001]



"""
Finding Roots of a Function
Find roots of 

f(x)=x 2−4."
"""

from scipy.optimize import root

def f(x):
    return x**2 - 4

# Solve for roots
result = root(f, x0=0)
print("Root:", result.x)

# output : Root: [2.]



