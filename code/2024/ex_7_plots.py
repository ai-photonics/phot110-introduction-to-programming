# Script which shows how to integrate using both Riemann sum and trapezium rule
#
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("WebAgg")

# Parameters
#
# The interval [A, B] to integrate over
A = 0; B = 2
# The number of pieces that we divide the interval in
N = 10
# Step-size of the points within the interval
dx = (B-A)/N

# x-coordinates defined as a Numpy array, these
xs = np.linspace(A, B, N+1)
# For the Trapezium method we need the y-coordinates computed from the original x-coordinates (not center points)
ys = xs**3 - xs/3
# For the Riemann sum we use the center points of the line pieces
xs_middle = xs + dx/2
xs_middle = xs_middle[:-1]
# We compute the y-coordinates of the x-coordinates at the centers
ys_middle = xs_middle**3 - xs_middle/3

print(xs)
print(xs_middle)

# We plot the function which we will integrate over interval [A, B] = [0, 2]
fig, ax = plt.subplots()
ax.plot(xs, ys)
plt.title("Function x^3 - x/3")

# We can solve the integral analytically
I_analytic = (B**4 / 4 - B**2 / 6) - (A**4 / 4 - A**2 / 6)
# (1) The Riemann sum is the sum of the rectangles with as height the middle points
I_riemann_manual = np.sum(ys_middle * dx)
# (2) The trapezium method calculates the sum of the areas of the trapeziums
I_trapz_manual = np.sum((ys[1:] + ys[:-1])) * dx / 2
# (3) The trapezium method is also incorporated within a Numpy function as is an often employed method
I_trapz = np.trapz(ys, xs, dx)

# We print all the results and their errors (difference with the analytically obtained solution) to compare.
print(f"Analytically calculated: {I_analytic}")
print(f"Riemann sum by hand: {I_riemann_manual}, error is {I_riemann_manual - I_analytic}")
print(f"Trapezium rule by hand: {I_trapz_manual}, error is {I_trapz_manual - I_analytic}")
print(f"Trapezium rule using numpy.trapz: {I_trapz}, error is {I_trapz - I_analytic}")

# The show() command is in the end not to block the execution of the rest of the script
plt.show()
