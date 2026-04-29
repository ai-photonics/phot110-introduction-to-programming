import numpy as np

A = np.array([[1, 1, 0],[1,1,1],[2,0,-1]])
b = np.array([0, 5, -2])
xyz = np.linalg.inv(A) @ b
print(A)
print(b)
print(xyz)
