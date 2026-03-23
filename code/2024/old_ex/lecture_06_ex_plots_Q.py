# Script which showcases some basic plotting using Matplotlib
#
# To help us to visualize numerical output we will use
# Matplotlib to plot curves (later on we will
# see how to make more specialized graphs with complex 2D
# or 3D data)

# Import statements
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("WebAgg")
import numpy as np
# ex 1: plot x^2 curve between -2 and 2 using
# for loops to generate the coords
# Syntax hint:
# for x in <sequence>
#   <statement>...
A = -2; B = 2; N = 10; dx = 1 / N
xs = []; ys = []
dx = (B - A) / N

for i in range(0, N+1):
    x = A + i * dx
    y = x ** 2
    xs.append(x)
    ys.append(y)
    # print(x)

print(xs)
print(ys)

fig, ax = plt.subplots()
ax.plot(xs, ys)
fig, ax = plt.subplots()
ax.plot(xs, ys)
# plt.plot(xs, ys)

# ex 2: plot x^2 curve between -2 and 2 using
# list comprehension to generate the coordinates
# Syntax hint: [fct(x) for x in <sequence>]

# ex 3: plot x^2 curve between -2 and 2 using
# arrays and the Numpy linspace function for the
# x-coordinates

# ex 4: plot cos() curve between 0 and 2*pi using
# arrays and the Numpy linspace and cos function
# for the x-coordinates

xs = np.linspace(0, 2 * np.pi, N)
ys = np.cos(xs)
fig, ax = plt.subplots()
ax.plot(xs, ys)
print(xs)
print(ys)

# ex 5: plot lissajoux curves (think: oscilloscope):
# The traversed coordinates are given by (x, y) which
# sinusoidal signals, with a phase difference: dphi and
# frequencies fx and fy in time t
#   x = sin(fx*t + dphi)
#   y = sin(fy*t)
#
# Use fx = 2..8, dphi = pi/2 or pi/4, and fy = fx - 1
# Use Numpy arrays, linspace (for time t), pi, and sin functions
#
# Hint: take time in interval [0, 2*pi], e.g.:
#   t = np.linspace(0, 2*np.pi, 1000)
#
plt.show()
