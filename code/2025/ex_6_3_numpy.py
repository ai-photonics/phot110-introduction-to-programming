# Practical 6: exercise 3
import numpy as np


# Create an array containing: `[1, 2, 3, 4, 5]`
a = np.arange(1, 6, 1)
print(a)

# Create an array using `np.linspace(start, stop, step)` with 20 elements equally spaced in the interval $[-2, 1]$
# Create an array using `np.arange(start, stop, step)` with inter-element distance of 0.5 for the same interval $[-2, 1]$


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
