import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

result = np.matmul(A, B)

result1 = A @ B

print("Using @:", result1)
print(result)
