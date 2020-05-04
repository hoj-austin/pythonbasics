import numpy as np

"""
Numpy basics
"""

# basic arrays - think matrices
a = np.array([[1,2], [1,1], [0,0]])
print(np.shape(a))  # (3, 2)
print(np.ndim(a))   # 2

# operators and methods
x = np.array([[2,0],[0,2]])
y = np.array([[1,1],[2,2]])
print(x*y)  # element-wise multiplication of equal shape arrays

newArray = np.arange(0, 10, 3)  # creates 1D array with constant spacing
print(newArray)

newArray = np.linspace(0, 10, 3)    # creates 1D array with constant spread (note the difference)
print(newArray)

