# Practical 6: exercise 3
import numpy as np


# Create an array containing: `[1, 2, 3, 4, 5]`
a = np.arange(1, 6, 1)
print(a)

# Create an array using `np.linspace(start, stop, step)` with 20 elements equally spaced in the interval $[-2, 1]$
b = np.linspace(-2, 1, 20)
print(b)

# Create an array using `np.arange(start, stop, step)` with inter-element distance of 0.5 for the same interval $[-2, 1]$
c = np.arange(-2, 1, 0.5)
print(c)
