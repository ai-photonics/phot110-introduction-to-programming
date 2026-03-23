# This script showcases the usage of random numbers in Numpy

# First we import the required libraries (numpy and matplotlib)
# Import numpy and matplotlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("WebAgg")

# ex 1: Generate 10000 random numbers with a normal distribution and plot the histogram
#   First initialize the random number generator
rng = np.random.default_rng(1)
#   - use the random number generator we created to generate 10000 random numbers from the standard normal distribution:
#       xs = rng.normal(size=10000)
#   - plot a histogram
#       ax.hist(x_uniform, 100)

# with a Gaussian (normal) distribution
x = rng.standard_normal(size=10000)
fig, ax = plt.subplots()
ax.hist(x, 100)

# ex 2: Generate random numbers from a normal distribution for both x and y coordinates and plot them in a scatterplot
#   - use the random number generator we created to generate 1000 random numbers for both x and y coordinates,
#     fill in loc(=mean), and scale(=sigma) as extra parameters:
#       xs = rng.normal(loc=4, scale=0.9, size=1000)
#       ys = rng.normal(loc=-2, scale=1.5, size=1000)
#   - plot a scatter plot with these as coordinates
#       ax.scatter(xs, ys)

# Number of random points
n_points = 1000

# Generating the x and y coordinates from Gaussian(=normal) distributions
x_mu = 4; x_sigma = 0.9
y_mu = -2; y_sigma = 1.5
xs = rng.normal(loc=x_mu, scale=x_sigma, size=n_points)
ys = rng.normal(loc=y_mu, scale=y_sigma, size=n_points)

# Plot the points using a scatter plot
fig, ax = plt.subplots()
ax.scatter(xs, ys)

# ex 3: Adapt the scatter plot of exercise 2 by specifying the size and color of the dots
#       ax.scatter(xs, ys, sz, colors, cmap=matplotlib.colormaps["jet"])
# where both sz and colors can be arrays of the same size as the coordinates or scalars
#       - for the size use for example 10
#       - for the colors create an array containing the distance of the coordinates to the center of the distribution
#       - the cmap argument allows us to set the colormap used

# Number of random points
n_points = 1000

# Generating the x and y coordinates from Gaussian(=normal) distributions
x_mu = 4; x_sigma = 0.9
y_mu = -2; y_sigma = 1.5
xs = rng.normal(loc=x_mu, scale=x_sigma, size=n_points)
ys = rng.normal(loc=y_mu, scale=y_sigma, size=n_points)

# The colors will be used in the scatter plot, they automatically will be scaled to the colormap.
# We use the (Euclidian) distance between the points and the center of the Gaussian distribution.
colors = np.sqrt((xs - x_mu)**2 + (ys - y_mu)**2)

# Plot the points using a scatter plot
fig, ax = plt.subplots()
ax.scatter(xs, ys, 10, colors, cmap=matplotlib.colormaps["jet"])
ax.set_aspect('equal', 'box')

# Use plt.show() only at the end of the script to prevent blocking the running script when using "WebAgg"
plt.show()
