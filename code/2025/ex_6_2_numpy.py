# Practical 6: exercise 2
import numpy as np

# Create a 3x3 array and fill the last column with numbers 1, 2, 3
a = np.empty(shape=(3, 3))
a[:, -1] = [1, 2, 3]
print(a)

# Extract the first row using the colon operator similar to lists
b = a[0, :]
print(b)

# Print the diagonal numbers using a loop
for i in range(len(a)):
    print(a[i, i])
