import numpy as np  

A = np.random.rand(3,3)
B = np.random.rand(3,3)

C = A @ B

print("Shape of A:", A.shape)
print("Shape of B:", B.shape)

print("Matrix A: \n", A)
print("Matrix B: \n", B)
print("Result:\n", C)
