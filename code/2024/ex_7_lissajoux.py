# ex 5: plot lissajoux curves (think: oscilloscope):
# The traversed coordinates are given by (x, y) which
# sinusoidal signals, with a phase difference: dphi and
# frequencies fx and fy in time t
#   x = sin(fx*t + dphi)
#   y = sin(fy*t)
#
# Use fx = 3, dphi = pi/2 or pi/4, and fy = fx - 1
# Use Numpy arrays, linspace (for time t), pi, and sin functions
#
# Hint: take time in interval [0, 2*pi], e.g.:
#   t = np.linspace(0, 2*np.pi, 1000)
#

# Import statements
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("WebAgg")

# Define the time interval
ts = np.linspace(0, 2*np.pi, 1000)
dphi = np.pi/2

fx = 3; fy = fx - 1
xs = np.sin(fx * ts + dphi)
ys = np.sin(fy * ts)
fig, ax = plt.subplots()
ax.plot(xs, ys)
plt.title(f"fx = {fx}, fy = {fy}")

# Now we plot the Lissajoux figures for each fx in [2..8]
# to showcase the different results.
for fx in range(2, 9):
    fy = fx - 1
    xs = np.sin(fx*ts + dphi)
    ys = np.sin(fy*ts)
    fig, ax = plt.subplots()
    ax.plot(xs, ys)
    plt.title(f"fx = {fx}, fy = {fy}")

plt.show()
