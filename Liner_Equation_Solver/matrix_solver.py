import numpy as np

# coefficient matrix
A = np.array([
    [2, 1],
    [1, 1]
])

# result vector
b = np.array([5, 3])

# solve Ax = b
x = np.linalg.solve(A, b)

print("Solution:", x)
