import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("WebAgg")
import numpy as np

class Figure():
    """
    This class is defined to showcase operator overloading.
    The Figure class allows creating a polygon by providing
    x,y coordinates (Numpy arrays).
    Two Figure objects can be multiplied by each other, in
    this test this just add the coordinates of the second
    Figure object to the coordinates of the first.
    """

    # Constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def plot(self):
        x_tmp = np.hstack([self.x, self.x[0]])
        y_tmp = np.hstack([self.y, self.y[0]])
        plt.plot(x_tmp, y_tmp)
        plt.show()

    def __mul__(self, other):
        f = Figure(np.hstack([self.x, other.x]),
                   np.hstack([self.y, other.y]))
        return f


# Define a first Figure object: a triangle
x = np.array([0, 2, 1])
y = np.array([0, 0, 2])
triangle = Figure(x, y)
# Define a second Figure object: a square polygon
x = np.array([0, 1, 1, 0])
y = np.array([0, 0, 1, 1])
square = Figure(x, y)

# Use the multiplication operator to multiply the two Figure objects:
f = triangle * square
# Plot the resulting Figure object:
f.plot()
