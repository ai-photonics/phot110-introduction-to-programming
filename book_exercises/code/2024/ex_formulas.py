import numpy as np


# helper functions
def area(radius):
    A = np.pi * radius ** 2
    return A

# script
a = 2
x = 4
y = 4 * (a * x) / (1 + np.sin(x))
print(y)

