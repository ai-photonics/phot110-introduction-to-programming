# Script which showcases some basic plotting using Matplotlib
#
# To help us to visualize numerical output we will use
# Matplotlib to plot curves (later on we will
# see how to make more specialized graphs with complex 2D
# or 3D data)
#
# There is currently a small issue with the installation of the
# computers in the lab, Matplotlib uses a library ("tkinter") normally
# available on Ubuntu for "asking the OS for a window" (to show
# a plot inside the window). This is called the "backend" that
# Matplotlib uses.
# The computers in the computer lab are new, and tkinter is not
# installed by accident. The IT staff is working on a solving this
# issue. For now, we can use "WebAgg" as an alternative backend.
# Therefore:
#
# (1) install the "tornado" package (a web-server), and
# select the "WebAgg" backend option in your script:
#   import matplotlib
#   matplotlib.use("WebAgg")
#
# (2) Further, to have all plots of the script within 1 browser tab
# we will use the command "plt.show()" only at the end, after
# defining all plots. I commented out the following lines within the script:
# plt.plot(xs, ys)
# plt.show()
# You can "uncomment" (by removing the hash symbols) them when not using WebAgg
#
# (3) For plotting a figure, you can use
#   fig, ax = plt.subplots()
#   ax.plot(xs, ys)


# Import statements
import matplotlib.pyplot as plt
import numpy as np
# The following two lines are to change the backend
import matplotlib
matplotlib.use("WebAgg")

# ex 1: plot x^2 curve between -2 and 2 using
# for loops to generate the coordinates
print("Ex 1")

# Parameters
start = -2; stop = 2; n = 10; step = 1 / n

# Grow the coordinates in the lists for x and y coordinates of the curve
xs = []; ys = []
for i in range((stop - start)*n + 1):
    x = start + i*step
    xs.append(x)
    ys.append(x**2)

# Plot the figure (Not showing it yet)
fig, ax = plt.subplots()
ax.plot(xs, ys)
print("END Ex 1\n")

# ex 2: plot x^2 curve between -2 and 2 using
# list comprehension to generate the coordinates
print("Ex 2")
start = -2; stop = 2; n = 10; step = 1 / n
xs = [start + i*step for i in range((stop - start)*n + 1)]
ys = [x**2 for x in xs]

fig, ax = plt.subplots()
ax.plot(xs, ys)
# plt.plot(xs, ys)
# plt.show()
print("END Ex 2\n")

# ex 3: plot x^2 curve between -2 and 2 using
# arrays and the Numpy linspace() function for the
# x-coordinates
print("Ex 3")
xs = np.linspace(start, stop, 4*n)
ys = xs**2

fig, ax = plt.subplots()
ax.plot(xs, ys)
# plt.plot(xs, ys)
# plt.show()
print("END Ex 3\n")

# ex 4: plot a cosine curve between 0 and 5*pi using
# arrays and the Numpy linspace() and cos() function
# for the x-coordinates
print("Ex 4")
xs = np.linspace(0, 5*np.pi, 100)
ys = np.cos(xs)

fig, ax = plt.subplots()
ax.plot(xs, ys)
# plt.plot(xs, ys)
# plt.show()
print("END Ex 4\n")

# Showing all plots on a single webbrowser tab
plt.show()
