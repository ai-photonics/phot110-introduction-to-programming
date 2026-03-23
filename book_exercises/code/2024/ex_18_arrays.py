import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("WebAgg")

# np.linspace(start, stop, number_of_points)
# Example linspace
x = np.linspace(0, 5, 16)
print(x)

# Example arange
x = np.arange(0, 5, 1.33)
print(x)

# Example meshgrid
y = 2*x
xx, yy = np.meshgrid(x, y)
print(yy)

