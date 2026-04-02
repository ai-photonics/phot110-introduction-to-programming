import numpy as np


def laplace(mat):
    n = mat.shape[0]
    det = 0
    if n > 1:
        for j in range(n):
            minor = np.delete(mat[1:, :], j, axis=1)
            # print(minor)
            det = det + (-1) ** j * mat[0, j] * laplace(minor)
    else:
        det = mat[0, 0]

    return det


# Define a matrix
mat = np.array([[1, 0, 0], [1, 2, -1], [0, 4, 9]])

# Calculate the determinant using our recursive function
det = laplace(mat)
print(f"Determinant calculated by our function: {det}")

# Compare with Numpy's linalg.det() function
det_numpy = np.linalg.det(mat)
print(f"Determinant calculated by numpy: {det_numpy}")
